from greener.forms import CreateEmployeeUser, ProgramForm
from helpers.funcs import generate_username_code
from django.shortcuts import render
from authentication.models import Profile
from helpers.data import DAYS
# Create your views here.

def home(request):
  return render(request, 'greener/index.html');



def register_employee(request):
  context = {
    'code': generate_username_code()
  }
  
  if request.method == 'POST':
    print(request.POST)
    form = CreateEmployeeUser(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
      user = form.save()
      print(user)
      profile = Profile.objects.create(user=user, fullname=request.POST.get('first_name'), user_role='host', phone=form.cleaned_data.get('phone'))
      profile.save()
      context['success'] = True
    else:
      context['error'] = True
      print(form.errors.as_data())
   
  return render(request, 'greener/register_employee.html', context);


def list_employee(request):
  query = Profile.objects.all()
  context = {
    'employees': query
  }
  return render(request, 'greener/list_employee.html', context);

def create_program(request, pk):
  form = ProgramForm()
  context = {'days': DAYS, 'host': pk }
  profile = Profile.objects.get(id=pk)
  if request.method == 'POST':
    form = ProgramForm(request.POST)
    day = DAYS[int(request.POST.get('day'))][0]
    if form.is_valid():
      print('Passed')
      form.save()
      
    else:
      print(form.errors.as_data())
  
  return render(request, 'greener/create_program.html', context);

def list_program(request):
  return render(request, 'greener/list_program.html');

def sponsorship(request):
  return render(request, 'greener/sponsorship.html');

def announcement(request):
  return render(request, 'greener/announcement.html');
