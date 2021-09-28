from django import forms
from django.core.exceptions import ValidationError

class CustomLoginForm(forms.Form):
  username = forms.CharField(max_length=10)
  password = forms.CharField(max_length=200)
  
  
  
  def validate(self):
    data = super().validate()
    if len(data > 10):
      raise ValidationError('Username exceeds 10 charaters')
    
    return data
    
    
  def save(self, commit=True):
    cleaned_data = super().save(commit=False)
    
    print('LOGIN FORM')
    
    if commit:
      print('Commited')