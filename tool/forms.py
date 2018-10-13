from django import forms

class ClassForm(forms.Form):
    building_name = forms.CharField()
    floor = forms.CharField()
