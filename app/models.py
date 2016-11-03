from django.db import models 
from django.contrib.auth.models import User

class Citation(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    link = models.URLField()
    notes = models.CharField(max_length=280)
    
