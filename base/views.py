from django.shortcuts import render
from api import views
import requests

# Create your views here.
def base(request):
  response = requests.get('http://127.0.0.1:8000/api/getData')
  data = response.json()
  return render(request, 'base.html', { 'data': data })