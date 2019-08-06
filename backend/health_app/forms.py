from .models import Profile,Extracted_data, Original_image
from django import forms

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewOriginalForm(forms.ModelForm):
    class Meta:
        model = Original_image
        exclude = ['posted_by']

class ScannForm(form.Form):
    image = forms.ImageField(upload_to = 'scan/')

class ExtractedForm(forms.ModelForm):
    class Meta:
        model = Extracted_data
        exclude = ['original','posted_by']