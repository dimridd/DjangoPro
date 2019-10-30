from django.db import models
from datetime import datetime
import django

class UserDetail(models.Model):
	email = models.CharField(max_length=200)
	First_Name = models.CharField(max_length=200)
	Middle_Name = models.CharField(max_length=200)
	Last_Name = models.CharField(max_length=200)
	
	tutorial_published = models.DateTimeField("date published", default=django.utils.timezone.now)



	def __str__(self):
		return self.email