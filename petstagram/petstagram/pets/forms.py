from django import forms
from petstagram.pets.models import Pet


class BaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_pet_photo']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',

                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={

                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date'
                }
            ),
            'personal_pet_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Like to image'
                }
            )
        }


class PetAddForm(BaseForm):
    pass


class PetEditForm(BaseForm):
    pass


class PedDeleteForm(forms.ModelForm):
    pass
