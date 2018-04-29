from django.urls import path, include
from . import views

urlpatterns = [
    # Login Gate
    path('', views.login_gate, name='login_gate'),
    # Dashboard
    path('home/dashboard/', views.dashboard, name='dashboard'),
]
