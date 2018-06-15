from django.forms import ModelForm, TextInput, forms
from .models import City


class CityForm(ModelForm):

    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input',
                                     'placeholder': 'City Name'}),
        }

    # def clean(self):
    #     data = self.cleaned_data
    #     if City.objects.filter(name=data['name']).exists():
    #         raise forms.ValidationError('Ya existe en la bd')

    #     # return data
    #     if City.objects.filter(name=self.cleaned_data['name']).exists():
    #         raise forms.ValidationError('ya existe en la bd')"""
    #
