from django.urls import path, include
from . import views

urlpatterns = [
    # Settings
    path('settings/', views.settings, name='settings'),
]
