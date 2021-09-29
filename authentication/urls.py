from django.urls import path
from .views import index, signOut


app_name = 'authentication'

urlpatterns = [
  path('', index, name='sign_in'),
  path('logout', signOut, name='sign_out'),
]