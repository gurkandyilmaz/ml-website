from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import QueryForm, PredictionForm, TitanicQueryForm, TitanicPredictionForm
from .models import Query, Prediction, TitanicQuery, TitanicPrediction

import os
import joblib
import numpy as np 

ml_models_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml-models-joblib')

print(ml_models_directory)

regressor_path = os.path.join(ml_models_directory, 'linear_regressor.joblib')
r2_scorer_path = os.path.join(ml_models_directory, 'r2_scorer.joblib')

with open(regressor_path, 'rb') as reg:
	regressor = joblib.load(reg)

with open(r2_scorer_path, 'rb') as r2:
	r2_scorer = joblib.load(r2)

x = [[5],[7],[8],[9]]
y = [5,6,7,7]

y_predicted = regressor.predict(x)
r2_score = r2_scorer(y,y_predicted)

# Create your views here.
def model_1(request):
	context = {'y_predicted': y_predicted, 'r2_score': r2_score, 'x':x, 'y':y, "model_1_status": "active"}

	return render(request, 'machine_learning/model_1.html', context=context)


def model_2(request):
	context = {"model_2_status": "active"}

	if request.method == 'POST':
		query_form = QueryForm(request.POST)
		if query_form.is_valid():
			query = query_form.save(commit=False)		
			query.query_time = timezone.now()
			query.save()
			
			query_converted = []
			for q in query.query_text.split(","):
				q = float(q)
				query_converted.append([q])

			query_predicted = np.round(regressor.predict(query_converted),4)
			query_prediction = zip(query_converted, query_predicted)
			if len(y) == len(query_predicted):
				r2 = r2_scorer(y, query_predicted)
			r2 = 0.0
			related_query = Query.objects.get(query_text=query.query_text, pk=query.id)

			prediction = Prediction(related_query=related_query, prediction_result=query_predicted, prediction_score=r2)
			prediction.save()

			return render(request, 'machine_learning/model_2.html', context={'form': query_form, 'y_predicted':query_predicted, 'query_prediction':query_prediction, 'r2_score':r2})

	else:
		query_form = QueryForm()
		query_predicted = "No predictions Available"


	return render(request, 'machine_learning/model_2.html', context={'form': query_form, 'y_predicted':query_predicted, 'model_2_status':"active"})


def model_3(request):
	context = context = {"model_3_status": "active"}

	standart_scaler_path = os.path.join(ml_models_directory, 'standart_scaler.joblib')
	knn_clf_path = os.path.join(ml_models_directory, 'knn_clf.joblib')

	with open(standart_scaler_path, 'rb') as stdscaler:
		standart_scaler = joblib.load(stdscaler)


	with open(knn_clf_path, 'rb') as knnclf:
		knn_clf = joblib.load(knnclf)


	if request.method == 'POST':
		query_form = TitanicQueryForm(request.POST)
		if query_form.is_valid():
			query = query_form.save(commit=False)		
			query.query_time = timezone.now()
			query.save()

			related_query = TitanicQuery(id=query.id)
			
			passenger_class = query_form.cleaned_data.get("passenger_class")
			passenger_gender = query_form.cleaned_data.get("passenger_gender")
			passenger_age = query_form.cleaned_data.get("passenger_age")
			sibling_spouse = query_form.cleaned_data.get("sibling_spouse")
			parent_children = query_form.cleaned_data.get("parent_children")
			passenger_fare = query_form.cleaned_data.get("passenger_fare")

			passenger_gender = 1 if passenger_gender=='male' else 0
			query_array = np.array([passenger_class, passenger_gender, passenger_age, sibling_spouse, parent_children, passenger_fare]).reshape(1,6)
			scaled_query_array = standart_scaler.transform(query_array)

			predicted_category = knn_clf.predict(scaled_query_array)
			probability = knn_clf.predict_proba(scaled_query_array)

			prediction = TitanicPrediction(related_query=related_query, 
											prediction_result=predicted_category[0], 
											prediction_probability_0=probability[0][0], 
											prediction_probability_1=probability[0][1],
											prediction_time=timezone.now())
			prediction.save()

			if predicted_category[0] == 1:
				category_predicted = "Survived"
			elif predicted_category[0] == 0:
				category_predicted = "Died"
			
			probability = 100*np.round(max(probability[0]), 4)
			
			return render(request, 'machine_learning/model_3.html', context={'form': query_form, 'predicted_category':category_predicted, 'probability':probability})

	else:
		query_form = TitanicQueryForm()
		query_predicted = "No predictions Available"

	return render(request, 'machine_learning/model_3.html', context={'form':query_form, 'model_3_status':'active'})