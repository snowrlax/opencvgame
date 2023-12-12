# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # Add other fields as needed

class saveEmail(models.Model):
    Email = models.EmailField()