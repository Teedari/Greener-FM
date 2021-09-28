from uuid import uuid5
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(to=User, related_name='user', on_delete=models.CASCADE)
  fullname = models.CharField(max_length=200)
  phone = models.CharField(max_length=10)
  user_role = models.CharField(max_length=10)
  
  def __str__(self):
    return self.fullname
  
  @property
  def email(self):
    return self.user.email
  
