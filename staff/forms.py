from django import forms
from .models import Tutor
from django.contrib.auth.models import User


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = [
            'name',
            'position',
            'load',
            'additional_work',
            'workplace',
            'disciplines'
        ]
        widgets = {
            'disciplines': forms.CheckboxSelectMultiple,
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
