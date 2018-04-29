from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from profile_app.models import ProfileSettings

# DESKs
class Desk(models.Model):
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='deks_images/', blank=False, null=False
    )
    CATEGORY_CHOICES = (
        ('WORLD', 'World'),
        ('POLITICS', 'Politics'),
        ('BUSINESS', 'Business'),
        (),
        (),
        (),
        (),
        (),
        (),
    )
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = 0

    def __str__(self):
        return self.name

'''# User ARTICLE(POST)
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_settings = models.ForeignKey(
            ProfileSettings, on_delete=models.CASCADE, blank=True, null=True
        )
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    CATEGORY_CHOICES = (
        ('POLITICS', 'Politics'),
        ('BUSINESS', 'Business'),
        ('TECH', 'Tech'),
        ('OPINION', 'Opinion'),
        ('SCIENCE', 'Science'),
        ('HEALTH', 'Health'),
        ('SPORTS', 'Sports'),
        ('ARTS', 'Arts'),
        ('FOOD', 'Food'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    PUBLICATION_TYPE_CHOICES = (
        ('AKUTEL', 'Akutel'),
        ('SPOT', 'Spot'),
        ('SO', '140Journos SO'),
        ('WHATSAPP', 'Whatsapp'),
        ('FACEBOOK', 'Facebook'),
    )
    publication_type = models.CharField(
            max_length=20, choices=PUBLICATION_TYPE_CHOICES
        )
    def __str__(self):
        return self.title
'''
