from django.contrib import admin
from django import forms
from .models import Item, Note

admin.site.register(Item)
admin.site.register(Note)
