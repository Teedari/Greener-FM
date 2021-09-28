from django.urls import path
from .views import home, register_employee, list_employee, create_program, list_program, announcement, sponsorship


app_name = 'greener'

urlpatterns = [
  path('', home , name='index'),
  
  path('employee/add', register_employee , name='add_employee'),
  
  path('employee/view', list_employee , name='view_employees'),
  
  path('program/create/<str:pk>', create_program , name='create_program'),
  
  path('program/view', list_program , name='view_programs'),
  
  path('annoucement', announcement , name='announcement'),
  path('sponsorship', sponsorship , name='sponsorship'),
]