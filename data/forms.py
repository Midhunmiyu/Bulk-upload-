from django import forms

from data.models import Person


class PersonData(forms.ModelForm):
    class Meta:
        model = Person
        field = '__all__'
