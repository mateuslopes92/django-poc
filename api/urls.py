from django.urls import path
from . import views

urlpatterns = [
  path('getData', views.getData),
  path('addItem', views.addItem),
]