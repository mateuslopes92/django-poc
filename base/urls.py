from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
  path('', views.BaseView.as_view(), name='base'),
  path('<int:pk>/', views.SingleView.as_view(), name='single'),
  path('add/', views.AddView.as_view(), name='add'),
]