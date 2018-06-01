from django.test import TestCase
from django.contrib.auth.models import User
from home_app.models import Office, OfficeWorkers, Announcament
from django.urls import reverse
from home_app.forms import NormalAccountForm, OfficeAccountForm


# Testing the normal account creation
class TestNormalAccountForm(TestCase):

    def test_form(self):
        form_data = {
            'username': 'hello',
            'email': 'hello@hello.com',
            'first_name': 'hello',
            'last_name': 'hello',
            'password': '123',
            'office_key': '123',
        }
        form = NormalAccountForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestOfficeAccountForm(TestCase):

    def test_form(self):
        form_data = {
            'office_name': 'test_name',
            'office_type': 'JOURNALISM',
            'username': 'test_username',
            'email': 'test@test.com',
            'first_name': 'test_firstname',
            'last_name': 'test_lastname',
            'password': '123',
        }
        form = OfficeAccountForm(data=form_data)
        self.assertTrue(form.is_valid())
