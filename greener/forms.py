from helpers.funcs import separate_fullname
from django.contrib.auth.models import User
from django import forms
from .models import Program



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
    user.set_password = self.cleaned_data.get('phone')

    if commit:
      user.save()
      # profile.user = user
      # profile.save()
      # print('User form saved successfully', profile)
      
    # user.set_password(self.cleaned_data.get('phone'))
    return super().save()
    
class ProgramForm(forms.ModelForm):
  class Meta:
    model = Program
    fields = '__all__'
    exclude = ['sponsorship', 'announcement', 'day']
    
    
  def save(self, commit=True, profile=None):
    instance = super().save(commit=False)
    instance.host = profile
    if commit:
      print(instance)
      instance.save()
      return super().save()
      