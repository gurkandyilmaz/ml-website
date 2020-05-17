from django import forms

from .models import Query, Prediction, TitanicQuery, TitanicPrediction, TextProcessing, TextProcessingResult


class QueryForm(forms.ModelForm):
	query_text = forms.CharField(max_length=200, help_text="Enter the query like 1,2,3")

	class Meta:
		model = Query
		fields = ('query_text',)


class PredictionForm(forms.ModelForm):

	class Meta:
		model = Prediction
		fields = ('prediction_result', 'prediction_score',)


class TitanicQueryForm(forms.ModelForm):

	class Meta:
		model = TitanicQuery
		fields = ('passenger_gender','passenger_class', 'passenger_age', 'sibling_spouse', 'parent_children', 'passenger_fare',)
		help_texts = {
			'passenger_gender':'Passenger Gender',
			'passenger_class':'Passenger Class', 
			'passenger_age':'Passenger Age',
			'sibling_spouse':'Number of Siblings and Spouse',
			'parent_children':'Number of Parents and Children',
			'passenger_fare':'Passenger Fare (Ticket Cost)'}


class TitanicPredictionForm(forms.ModelForm):
	
	class Meta:
		model = TitanicPrediction
		fields = ('prediction_result', 'prediction_probability_0', 'prediction_probability_1',)


class TextProcessingForm(forms.ModelForm):

	class Meta:
		model = TextProcessing
		fields = ('text_area', 'language_choice', 'make_lowercase', 'remove_stopwords', 'remove_numbers', 'remove_html_tags', 'remove_special_characters', 'remove_url',)
		help_texts = {
			'language_choice':'Specify Language',
			'make_lowercase': 'Lowercase',
			'remove_stopwords': 'Stopwords',
			'remove_numbers':'Numbers',
			'remove_html_tags':'HTML',
			'remove_special_characters':'Special Characters',
			'remove_url':'URL',
			}
		widgets = {
            'text_area': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


# class TextProcessingResultForm(forms.ModelForm):

# 	class Meta:
# 		model = TextProcessingResult
# 		fields = ('text_result',)
# 		help_texts = {
# 			'text_result':'The result will be shown HERE'
# 			}
# 		widgets = {
#             'text_result': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
#         }