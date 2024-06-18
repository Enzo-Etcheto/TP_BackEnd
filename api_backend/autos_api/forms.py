from django import forms
from autos_api.models import Autos,User

class AutosForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = [
            'marca',
            'modelo',
            'color',
            'num_serie',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'auto',
        ]