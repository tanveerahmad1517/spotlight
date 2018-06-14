from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from desk_app.models import Desk


# DESK CREATE Form
class DeskCreateForm(ModelForm):
    class Meta:
        model = Desk
        fields = ['image', 'category', 'name', 'description']
        widgets = {
            
        }
