from django import forms

class FormForm(forms.Form):
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()