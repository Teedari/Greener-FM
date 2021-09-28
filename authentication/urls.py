from django.urls import path
from .views import index


app_name = 'authentication'

urlpatterns = [
  path('', index, name='sign_in')
]