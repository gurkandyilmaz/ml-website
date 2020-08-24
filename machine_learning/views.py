from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import TitanicQueryForm, TitanicPredictionForm, TextProcessingForm
from .forms import TelcoChurnQueryForm
from .models import TitanicQuery, TitanicPrediction, TextProcessing, TextProcessingResult
from .models import TelcoChurnQuery, TelcoChurnPrediction

# Preprocessing in model_1
from .ml_models_joblib.preprocess import Preprocess, select_parameters
# Churn data processing in model_2
from .ml_models_joblib.churn_data_process import churn_data_process

# model_2
import os
import joblib
import numpy as np


ml_models_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_models_joblib')


@login_required
def model_1(request):
	processor = Preprocess()

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
			language_choice = text_form.cleaned_data.get('language_choice')
			make_lowercase = text_form.cleaned_data.get('make_lowercase')
			remove_stopwords = text_form.cleaned_data.get('remove_stopwords')
			remove_numbers = text_form.cleaned_data.get('remove_numbers')
			remove_html_tags = text_form.cleaned_data.get('remove_html_tags')
			remove_special_characters = text_form.cleaned_data.get('remove_special_characters')
			remove_url = text_form.cleaned_data.get('remove_url')
			
			processed_text = select_parameters(raw_text, language_choice=language_choice, make_lowercase=make_lowercase, remove_stopwords=remove_stopwords, remove_numbers=remove_numbers, 
                      remove_html_tags=remove_html_tags, remove_special_characters=remove_special_characters, remove_url=remove_url)
			
			related_text = TextProcessing.objects.get(id=text.id)
			result_text = TextProcessingResult(related_text=related_text, text_result=processed_text, text_result_time=timezone.now())
			result_text.save()
					
			return render(request, 'machine_learning/model_1.html', context={"text_form":text_form, "result_text":result_text.text_result, "model_1_status": "active"})
	else:
		text_form = TextProcessingForm()

	return render(request, 'machine_learning/model_1.html', context={"text_form":text_form, "model_1_status": "active"})


@login_required
def model_2(request):

	churn_models_path = os.path.join(ml_models_directory, 'churn_models_v2.joblib')

	with open(churn_models_path, 'rb') as models_file:
		minmax_scaler, svc_clf, knn_clf, rand_clf, ada_clf = joblib.load(models_file)

	if request.user.is_authenticated:
		username = request.user.username

	if request.method == 'POST':
		query_form = TelcoChurnQueryForm(request.POST)

		if query_form.is_valid():
			query_churn = query_form.save(commit=False)		
			query_churn.query_time = timezone.now()
			query_churn.user = username
			query_churn.save()

			tenure = query_form.cleaned_data.get('tenure')
			internet_service = query_form.cleaned_data.get('internet_service')
			payment_method = query_form.cleaned_data.get('payment_method')
			
			svc_clf_status = query_form.cleaned_data.get('svc_clf')
			knn_clf_status = query_form.cleaned_data.get('knn_clf')
			rand_clf_status = query_form.cleaned_data.get('rand_clf')
			ada_clf_status = query_form.cleaned_data.get('ada_clf')
			
			# Process the form data to use in the clfs
			clfs = {'minmax_scaler':minmax_scaler, 'svc_clf':svc_clf, 'knn_clf':knn_clf, 'rand_clf':rand_clf, 'ada_clf':ada_clf}
			form_data = {'tenure':tenure, 'internet_service':internet_service, 'payment_method':payment_method}
			status = {'svc_clf_status':svc_clf_status,
			          'knn_clf_status':knn_clf_status,
			          'rand_clf_status':rand_clf_status,
			          'ada_clf_status':ada_clf_status}

			results = churn_data_process(clfs=clfs, form_data=form_data, status=status)
			related_query = TelcoChurnQuery(id=query_churn.id)
			prediction = TelcoChurnPrediction(related_query=related_query, 
				result_svc=results['svc_clf']['predicted_result'],result_proba_svc=results['svc_clf']['predicted_proba'],
				result_knn=results['knn_clf']['predicted_result'],result_proba_knn=results['knn_clf']['predicted_proba'],
				result_rand=results['rand_clf']['predicted_result'],result_proba_rand=results['rand_clf']['predicted_proba'],
				result_ada=results['ada_clf']['predicted_result'],result_proba_ada=results['ada_clf']['predicted_proba'],prediction_time=timezone.now())
			prediction.save()


			print("RESULTS: {0}".format(results))

			return render(request, 'machine_learning/model_2.html', context={'form':query_form, 'results':results, "model_2_status": "active"})

	else:
		query_form = TelcoChurnQueryForm()
		

	return render(request, 'machine_learning/model_2.html', context={'form':query_form, 'model_2_status':"active"})


@login_required
def model_3(request):

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
			
			probability = np.round_(100*max(probability[0]), decimals=2)
			
			return render(request, 'machine_learning/model_3.html', context={'form': query_form, 'predicted_category':category_predicted, 'probability':probability, 'model_3_status':'active'})
	else:
		query_form = TitanicQueryForm()
		query_predicted = "No predictions Available"

	return render(request, 'machine_learning/model_3.html', context={'form':query_form, 'model_3_status':'active'})


