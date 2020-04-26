from django import forms

from .models import Query, Prediction


class QueryForm(forms.ModelForm):

	class Meta:
		model = Query
		fields = ('query_text',)


class PredictionForm(forms.ModelForm):

	class Meta:
		model = Prediction
		fields = ('prediction_result', 'prediction_score',)