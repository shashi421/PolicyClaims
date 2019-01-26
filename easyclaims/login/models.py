from django.db import models
from datetime import datetime
class User(models.Model):
    user_id=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    postcode=models.IntegerField(default=None, blank=True, null=True)
    dob=models.DateField(default=None, blank=True, null=True)
    created_at=models.DateTimeField(default=datetime.now)
    class Meta:
        ordering = ['created_at']
# Create your models here.
