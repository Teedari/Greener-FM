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
  message = models.CharField(max_length=200, blank=True)
  def __str__(self):
    return f'{self.message}'

class Sponsorship(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200, blank=True)
  
  def __str__(self):
    return f'{self.name}'

class Program(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  days = models.CharField(choices=DAYS, max_length=20, default=DAYS[0][0], blank=True)
  time = models.TimeField(blank=True)
  sponsorship = models.ManyToManyField(to=Sponsorship,related_name='sponsorships', blank=True)
  announcement = models.ManyToManyField(to=Announcement,related_name='announcements', blank=True)
  host = models.OneToOneField(to=Profile,related_name='profile', on_delete=models.CASCADE, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return f'{self.title}'

  @property
  def all_annoucements(self):
    arr = [ announcement for announcement in self.announcement.all() ]
    result = [ ar.message for ar in arr ]
    print('Array ', result)
    
    return result
  
  
  @property
  def all_sponsorships(self):
    arr = [ sponsorship for sponsorship in self.sponsorship.all() ]
    result = [ ar.name for ar in arr ]
    print('Array ', result)
    return result
  
  # @property
  # def all_sponsorships(self):
  #   return [ sponsorship.name for sponsorship in self.sponsorship ]
