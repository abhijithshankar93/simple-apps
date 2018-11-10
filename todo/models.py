from django.db import models

# Create your models here.

class to_do_item(models.Model):
	content=models.TextField()