from django.urls import path
from .views import home, register_employee, list_employee, create_program, list_program, announcement, add_announcement , sponsorship , add_sponsorship, sponsorship_delete, announcement_delete


app_name = 'greener'

urlpatterns = [
  path('', home , name='index'),
  
  path('employee/add', register_employee , name='add_employee'),
  
  path('employee/view', list_employee , name='view_employees'),
  
  path('program/create/<str:pk>', create_program , name='create_program'),
  
  path('program/view', list_program , name='view_programs'),
  
  path('annoucement', announcement , name='announcement'),
  
  path('annoucement/add', add_announcement , name='add_announcement'),
  
  path('sponsorship', sponsorship , name='sponsorship'),
  
  path('sponsorship/<int:id>/delete', sponsorship_delete , name='sponsorship_delete'),
  
  path('annoucement/<int:id>/delete', announcement_delete , name='announcement_delete'),
  
  path('sponsorship/add', add_sponsorship , name='add_sponsorship'),
  
]