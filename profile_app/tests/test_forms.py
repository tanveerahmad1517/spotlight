from django.test import TestCase
from django.urls import reverse
from profile_app.forms import ProfileSettingsForm


# TESTING SETTINGS FORM
class TestingSettingsForm(TestCase):
    def test_form(self):
        form_data = {
            'profile_photo': 'hey.png',
            'bio': 'test bio',
            'personal_link': 'www.test.com'
        }
        bio = "test bio"
        personal_link = "hey.com"
        form = ProfileSettingsForm(bio, personal_link)
        self.assertTrue(form.is_valid())
