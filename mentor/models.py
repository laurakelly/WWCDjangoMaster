from django.db import models
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    website = forms.CharField()
    # mentor/mentee checkbox
    interests_skills = forms.CharField()
    neighborhood = forms.CharField()
    comments = forms.CharField()
