from django.urls import path

from . import views

# Urls are the website URLS that we can navigate to and we link them to a function that we create in .views
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.number, name='number'),
]
