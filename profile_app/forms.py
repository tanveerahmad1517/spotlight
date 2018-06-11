from django import forms
from django.forms import ModelForm
from profile_app.models import ProfileSettings


# SETTINGS FROM
class ProfileSettingsForm(ModelForm):
    class Meta:
        model = ProfileSettings
        fields = ['profile_photo', 'bio', 'personal_link']
