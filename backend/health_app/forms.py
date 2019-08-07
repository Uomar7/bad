from .models import Profile, Original_image
from django import forms

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewOriginalForm(forms.ModelForm):
    class Meta:
        model = Original_image
        exclude = ['posted_by','hiv','gender','visit','age']