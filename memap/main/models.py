from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager


class Item(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(null=True, blank=True, max_length=200)
	tags = TaggableManager(blank=True)
	
	def __str__(self):
		return self.name if self.name else "No title"


class Note(models.Model):
	item = models.ForeignKey(Item)
	text = models.TextField(blank=True, null=True)
	image = models.URLField(blank=True, null=True)
	audio = models.URLField(blank=True, null=True)
	video = models.URLField(blank=True, null=True)	
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text if self.text else "No title"