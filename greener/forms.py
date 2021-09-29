from django.db import models
from django.db.models import fields
from helpers.funcs import separate_fullname
from django.contrib.auth.models import User
from django import forms
from .models import Announcement, Program, Sponsorship



class CreateEmployeeUser(forms.ModelForm):
  phone = forms.CharField(max_length=10)
  class Meta:
    model=User
    fields = ['username','first_name', 'last_name', 'email', 'phone']
    
    
  def save(self, commit=True):
    user = super().save(commit=False)
    name = separate_fullname(self.cleaned_data.get('first_name'))
    user.first_name = name['first_name']
    user.last_name = name['last_name']
    user.set_password = 'Emission*12'

    if commit:
      user.save()

    return super().save()
    
class ProgramForm(forms.ModelForm):
  class Meta:
    model = Program
    fields = '__all__'
    exclude = ['sponsorship', 'announcement', 'days', 'host']
    
    
  def save(self, commit=True, profile=None):
    instance = super().save(commit=False)
    instance.host = profile
    if commit:
      print(instance)
      instance.save()
      return super().save()
      
      
class AnnouncementForm(forms.ModelForm):
  class Meta:
    fields = '__all__'
    model = Announcement
    
  def save(self, commit=True, pk = 1):
    announcement = super().save(commit=False)
    if commit:
      announcement.save()
      
    return super().save()
    
class SponsorshipForm(forms.ModelForm):
  class Meta:
    fields = '__all__'
    model = Sponsorship
    
  def save(self, commit=True):
    sponsorship = super().save(commit=False)
    if commit:
      sponsorship.save()
      
    return super().save()