from django import forms
from .models import MadLibsUserInput


class MadLibsUserInputForm(forms.ModelForm):
    class Meta:
        model = MadLibsUserInput
        fields = ['Noun',
                  'Noun2',
                  'Noun3',
                  'Person',
                  'Place',
                  'Thing',
                  'Adjective']
