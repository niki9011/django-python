from django import forms
from .models import Photo


class BaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['pet_image', 'description', 'location', 'tagged_pets']
        labels = {
            'pet_image': 'Photo file',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tag pets',
        }


class PhotoAddForm(BaseForm):
    pass


class PhotoEditForm(BaseForm):
    pass

