from django.urls import path, include
from . import views

urlpatterns = [
    # Contributions
    path('contributions/', views.contributions, name='contributions'),
    # Settings
    path('settings/', views.settings, name='settings'),
]
