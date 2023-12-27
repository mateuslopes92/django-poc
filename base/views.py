from django.shortcuts import render
from api import views
from .models import Item
from django.views.generic import ListView, DetailView
import requests

# Create your views here.
def base(request):
  response = requests.get('http://127.0.0.1:8000/api/getData')
  data = response.json()
  return render(request, 'base.html', { 'data': data })

class BaseView(ListView):
  model = Item
  template_name = 'base.html'

class SingleView(DetailView):
  model = Item
  template_name = 'single.html'
  context_object_name = 'item'