from django import forms
from .models import ImageCategory , ImageModel

class ImageUploadForm(forms.ModelForm):
    title = forms.CharField(max_length=50 , label='Image Title')
    image = forms.ImageField(label='Select an Image to Upload')
    category = forms.ModelChoiceField(queryset=ImageCategory.objects.all(), label='Select Category')

    class Meta:
        model = ImageModel
        fields = ['title', 'image', 'category']