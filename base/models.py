from django.db import models
from django.urls import reverse

class Item(models.Model):
  title =  models.CharField(max_length=200)
  description =  models.TextField(null=True)
  created = models.DateTimeField(auto_now_add=True)

  def get_absolute_url(self):
    return reverse('base:single', args=[self.id])

  class Meta:
    ordering = ['-created']

  def __str__(self):
    return self.title