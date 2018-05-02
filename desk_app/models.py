from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from profile_app.models import ProfileSettings

# DESKs
class Desk(models.Model):
    sub_editor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='deks_images/', blank=False, null=False
    )
    CATEGORY_CHOICES = (
        ('WORLD', 'fa fa-globe'),
        ('METRO', 'fa fa-building'),
        ('POLITICS', 'fa-flag'),
        ('BUSINESS', 'fa fa-suitcase'),
        ('TECH', 'fa fa-code'),
        ('SCIENCE', 'fa fa-flask'),
        ('OPINION', 'fa fa-gavel'),
        ('HEALTH', 'fa fa-heart'),
        ('SPORTS', 'fa fa-bicycle'),
        ('ARTS', 'fa fa-paint-brush'),
        ('BOOKS', 'fa fa-book'),
        ('STYLE', 'fa fa-eye'),
        ('TRAVEL', 'fa fa-plane'),
        ('MAGAZINE', 'fa fa-file'),
        ('TABLOID', 'fa fa-phone'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name
