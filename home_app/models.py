from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from profile_app.models import ProfileSettings


# Announcaments
class Announcament(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_settings = models.ForeignKey(
        ProfileSettings, on_delete=models.CASCADE, null=True, blank=True,
    )
    content = models.TextField(blank=False, null=False)
    publish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username
