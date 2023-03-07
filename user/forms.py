from django.contrib.auth.models import User
from django import forms
from .models import brainjaiib


class updatescore(forms.Form):
    subcode = forms.CharField(max_length=100)
    scoreobtained = forms.CharField(max_length=1)

    class Meta:
        model = brainjaiib
        fields = ['subcode','scoreobtained']
