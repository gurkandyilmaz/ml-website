from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import QueryForm, PredictionForm, TitanicQueryForm, TitanicPredictionForm, TextProcessingForm
from .models import Query, Prediction, TitanicQuery, TitanicPrediction, TextProcessing, TextProcessingResult

# Preprocessing in model_1
from .ml_models_joblib.preprocess import Preprocess, select_parameters

# model_2
import os
import joblib
import numpy as np


ml_models_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_models_joblib')

# Create your views here.
@login_required
def model_1(request):
	

	processor = Preprocess()
	#tokenized = processor.word_tokenize("Hi my name is grkn i am 45 years old and i like hiking.")

	if request.user.is_authenticated:
		username = request.user.username

	if request.method == "POST":
		text_form = TextProcessingForm(request.POST)
		

		if text_form.is_valid():
			text = text_form.save(commit=False)
			text.user = username
			text.processing_time = timezone.now()
			text.save()
			

			raw_text = text_form.cleaned_data.get('text_area')
			make_lowercase = text_form.cleaned_data.get('make_lowercase')
			remove_stopwords = text_form.cleaned_data.get('remove_stopwords')
			remove_numbers = text_form.cleaned_data.get('remove_numbers')
			remove_html_tags = text_form.cleaned_data.get('remove_html_tags')
			remove_special_characters = text_form.cleaned_data.get('remove_special_characters')
			remove_url = text_form.cleaned_data.get('remove_url')

			# Start preprocessing
			# tokenized_text = processor.word_tokenize(text.text_area)
			
			# stopwords_removed = processor.remove_stopwords(tokenized_text)
			# numbers_removed = processor.remove_numbers(text.text_area)
			# special_characters_removed = processor.remove_special_characters(text.text_area)
			# html_tags_removed = processor.remove_html_tags(text.text_area)
			# url_removed = processor.remove_url(text.text_area)
			processed_text = select_parameters(raw_text, make_lowercase=make_lowercase, remove_stopwords=remove_stopwords, remove_numbers=remove_numbers, 
                      remove_html_tags=remove_html_tags, remove_special_characters=remove_special_characters, remove_url=remove_url)
			
			related_text = TextProcessing.objects.get(id=text.id)
			result_text = TextProcessingResult(related_text=related_text, text_result=processed_text, text_result_time=timezone.now())
			result_text.save()
			# result_form = TextProcessingResultForm()			

			return render(request, 'machine_learning/model_1.html', context={"text_form":text_form, "result_text":result_text.text_result, "model_1_status": "active"})
	else:
		text_form = TextProcessingForm()
		# result_form = TextProcessingResultForm()

	return render(request, 'machine_learning/model_1.html', context={"text_form":text_form, "model_1_status": "active"})


@login_required
def model_2(request):
	context = {"model_2_status": "active"}

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


@login_required
def model_3(request):
	context = {"model_3_status": "active"}

	standart_scaler_path = os.path.join(ml_models_directory, 'standart_scaler.joblib')
	knn_clf_path = os.path.join(ml_models_directory, 'knn_clf.joblib')

	with open(standart_scaler_path, 'rb') as stdscaler:
		standart_scaler = joblib.load(stdscaler)


	with open(knn_clf_path, 'rb') as knnclf:
		knn_clf = joblib.load(knnclf)

	if request.user.is_authenticated:
		username = request.user.username

	if request.method == 'POST':
		query_form = TitanicQueryForm(request.POST)

		if query_form.is_valid():
			query = query_form.save(commit=False)		
			query.query_time = timezone.now()
			query.user = username
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
			
			return render(request, 'machine_learning/model_3.html', context={'form': query_form, 'predicted_category':category_predicted, 'probability':probability, 'model_3_status':'active'})

	else:
		query_form = TitanicQueryForm()
		query_predicted = "No predictions Available"

	return render(request, 'machine_learning/model_3.html', context={'form':query_form, 'model_3_status':'active'})


