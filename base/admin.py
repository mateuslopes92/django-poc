from django.contrib import admin
from .models import Item

@admin.register(Item)
class PostItem(admin.ModelAdmin):
  prepopulated_fields = {'title': ('title',), }
