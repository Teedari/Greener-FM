from django.db import models
from helpers.data import DAYS
from authentication.models import Profile
# Create your models here.

class Todo(models.Model):
  id = models.AutoField(primary_key=True)
  text = models.CharField(max_length=100)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
  id = models.AutoField(primary_key=True)
  message = models.TextField(blank=True)

class Sponsorship(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200, blank=True)

class Program(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  days = models.CharField(choices=DAYS, max_length=20, default=DAYS[0][0], blank=True)
  time = models.TimeField(blank=True)
  sponsorship = models.ManyToManyField(to=Sponsorship,related_name='sponsorships')
  announcement = models.ManyToManyField(to=Announcement,related_name='announcements')
  host = models.OneToOneField(to=Profile,related_name='announcements', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  


