from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Item
from django.views.generic import ListView, DetailView, CreateView
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

class AddView(CreateView):
  model = Item
  # fields = ['title', 'description']
  template_name = 'add.html'
  fields = '__all__'
  success_url = reverse_lazy('base')