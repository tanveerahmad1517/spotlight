from django.test import TestCase
from django.contrib.auth.models import User
from home_app.models import Office
from django.urls import reverse


# TESTING THE HOME VIEW
class TestHomeView(TestCase):

    def setUp(self):
        pass

    def test_view_exists_at_desired_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_is_accesible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_app/home.html')


# TESTING THE SIGNUP VIEW
class TestSignupView(TestCase):

    def setUp(self):
        pass

    def test_view_exists_at_desired_url(self):
        pass
