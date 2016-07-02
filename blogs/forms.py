from django import forms

class AddForm(forms.Form):
	title = forms.CharField(max_length=20)
	text = forms.CharField()
	date = forms.DateTimeField()
