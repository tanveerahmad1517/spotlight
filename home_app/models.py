from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from profile_app.models import ProfileSettings
import random
import string


# FUNCTIONS FOR MODELS
def generate_secret_key():
    return ''.join(
       random.choice(string.ascii_uppercase + string.digits) for _ in range(20)
    )


# USER ADITTIONS
class UserAdittion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_office = models.OneToOneField("Office", on_delete=models.CASCADE)

    def __str__(self):
        return user.username


# OFFICE
class Office(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_settings = models.ForeignKey(
            ProfileSettings, on_delete=models.CASCADE
    )
    admin_adittions = models.ForeignKey(UserAdittion, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    TYPE_CHOICES = (
        ("Journalism", "Journalism"),
    )
    type = models.CharField(max_length=250, choices=TYPE_CHOICES)
    secret_key = models.CharField(max_length=20, default=generate_secret_key)
    creation_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.office_name


# ANNOUNCAMENTS
class Announcament(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_settings = models.ForeignKey(
        ProfileSettings, on_delete=models.CASCADE, null=True, blank=True,
    )
    content = models.TextField(blank=False, null=False)
    publish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username
