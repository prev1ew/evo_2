from .models import Persons
from django.forms import ModelForm, TextInput


class PersonsForm(ModelForm):
    class Meta:
        model = Persons
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            })
        }
