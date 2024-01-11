from django import forms
from foodlens.models import Image
 
 
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image',)
