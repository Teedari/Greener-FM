from django.urls import path
from .views import index, announcements, sponsorships, user_programs


app_name = 'host'

urlpatterns = [
  path('index', index, name='index'),
  path('all_programs', user_programs, name='user_programs'),
  path('announcements', announcements, name='announcements'),
  path('sponsorships', sponsorships, name='sponsorships'),
]