# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Tutor

class TutorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'  
