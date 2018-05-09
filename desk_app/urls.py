from django.urls import path, include
from . import views

urlpatterns = [
    # TO-DO tasks page
    path('<str:deskname>/todo/', views.to_do, name='to_do'),
    # New Article create page
    path('<str:deskname>/article/new/', views.new_article, name='new_article'),
]
