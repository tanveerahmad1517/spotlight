from django.urls import path, include
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    # Login Gate
    path('home/login/', views.login_gate, name='login_gate'),
    # Dashboard
    path('home/dashboard/', views.dashboard, name='dashboard'),
    # Desk
    path('home/desk/', views.desk_browse, name='desk_browse'),
    # Search
    path("home/search/", views.search, name="search"),
    # Publish
    path("home/publish/", views.publish, name="publish"),
]
