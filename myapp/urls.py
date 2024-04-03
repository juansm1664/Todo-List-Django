from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
]
