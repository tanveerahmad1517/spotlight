from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:deskname>/', views.to_do, name='to_do'),
]
