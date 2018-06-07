from django.test import TestCase
from django.contrib.auth.models import User
from home_app.models import Office, OfficeWorkers, Announcament
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
        response = self.client.get("/home/signup/")
        self.assertEqual(response.status_code, 200)

    def test_view_is_accesible_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_app/signup.html')


# TESTING THE LOGIN VIEW
class TestLoginView(TestCase):

    def setUp(self):
        pass

    def test_view_exists_at_desired_url(self):
        response = self.client.get("/home/login/")
        self.assertEqual(response.status_code, 200)

    def test_view_is_accesible_by_name(self):
        response = self.client.get(reverse('login_gate'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login_gate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_app/login_gate.html')


# TESTING OFFICE DASHBOARD
class TestDashboardView(TestCase):

    def setUp(self):
        test_user = User.objects.create(username='test_user', password='123')
        test_office = Office.objects.create(
            name='test_office', admin=test_user
        )

    def test_view_kwargs(self):
        response = self.client.get(
            reverse('dashboard', kwargs={'officename': 'test_office', })
        )
        self.assertEqual(response.status_code, 302)

    def test_view_exists_at_desired_url(self):
        response = self.client.get("/test_office/dashboard/")
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        response = self.client.get("/test_office/dashboard/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_app/dashboard.html')
