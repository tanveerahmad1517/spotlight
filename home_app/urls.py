from django.urls import path, include
from . import views

urlpatterns = [
    # Login Gate
    path('', views.login, name='login'),
]
