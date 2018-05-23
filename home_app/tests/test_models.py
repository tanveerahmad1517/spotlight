from django.test import TestCase
from django.contrib.auth.models import User
from home_app.models import Office, OfficeWorkers


# TESTING THE OFFICE MODEL
class TestOffice(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        office = Office.objects.create(admin=user, name='test_office')

    def test_to_string(self):
        office = Office.objects.get(id=1)
        expected_to_string = "test_office"
        self.assertEqual(expected_to_string, str(office))


# TEST OFFICE WORKERS MODEL
class TestOfficeWorkers(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        office = Office.objects.create(admin=user, name='test_office')
        office_worker = OfficeWorkers.objects.create(user=user,
                                                     joined_office=office)

    def test_to_string(self):
        office_worker = OfficeWorkers.objects.get(id=1)
        expected_to_string = 'test_user'
        self.assertEqual(expected_to_string, str(office_worker))
