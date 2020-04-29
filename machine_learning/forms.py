from django import forms

from .models import Query, Prediction, TitanicQuery, TitanicPrediction


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
	# passenger_class = forms.IntegerField(help_text="Passenger Class")
	# passenger_age = forms.IntegerField(help_text="Passenger Age")
	# sibling_spouse = forms.IntegerField(help_text="number of siblings and spouse")
	# parent_children = forms.IntegerField(help_text="number of parent and children")
	# passenger_gender = forms.CharField(help_text="Passenger Gender")
	# passenger_fare = forms.DecimalField(help_text="Passenger Fare")


	class Meta:
		model = TitanicQuery
		fields = ('passenger_gender','passenger_class', 'passenger_age', 'sibling_spouse','parent_children', 'passenger_fare')

class TitanicPredictionForm(forms.ModelForm):
	pass