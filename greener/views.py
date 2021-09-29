from django.http.response import HttpResponse, HttpResponseRedirect
from greener.models import Announcement, Program, Sponsorship
from greener.forms import AnnouncementForm, CreateEmployeeUser, ProgramForm, SponsorshipForm
from helpers.funcs import generate_username_code
from django.shortcuts import render, reverse
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
    # print(request.POST)

    form = CreateEmployeeUser(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
      user = form.save()
      print(user)
      
      uUser = User.objects.get()
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
  # print('LOG 1: ', profile)
  try:
    # request.session['sponsorship']  
    # print(request.session['sponsorship'])
    context['sponsorship'] =  request.session['sponsorship'] 
    context['announcement'] =  request.session['announcement'] 
  except:
    print('Session not found')
  
  if request.method == 'POST':
    print('LOG 2: ', pk, profile)
    form = ProgramForm(request.POST)
    day = DAYS[int(request.POST.get('day'))][0]
    if form.is_valid():
      print('Passed', form.cleaned_data)
      program = Program.objects.create(host=profile, **form.cleaned_data, days=day)
      program.save()
    else:
      print(form.errors.as_data())
  request.session['host'] = profile.id
  return render(request, 'greener/create_program.html', context);

def add_sponsorship(request):
  pk = request.session['host']
  if request.method == 'POST':
    form = SponsorshipForm(request.POST)
    if form.is_valid():
      request.session['sponsorship'] = True
      sponsor = form.save()
      p = Program.objects.get(id=pk)
      p.sponsorship.add(sponsor)
      p.save()
    else:
      request.session['sponsorship'] = False
  
  return HttpResponseRedirect(reverse('greener:create_program', kwargs={'pk': pk}))
  

def add_announcement(request):
  pk = request.session['host']
  if request.method == 'POST':
    form = AnnouncementForm(request.POST)
    if form.is_valid():
      request.session['announcement'] = True
      announce = form.save()
      p = Program.objects.get(id=pk)
      p.announcement.add(announce)
      p.save()
    else:
      request.session['announcement'] = False
  
  return HttpResponseRedirect(reverse('greener:create_program', kwargs={'pk': pk}))

def list_program(request):
  program = Program.objects.all()
  context= {
    'programs': program
  }
  

  return render(request, 'greener/list_program.html', context);

def sponsorship(request):
  sponsor = Sponsorship.objects.all()
  context = {'sponsorships': sponsor}
  return render(request, 'greener/sponsorship.html', context);

def sponsorship_delete(request, id):
  try:
    spon = Sponsorship.objects.get(id=id)
    spon.delete()
  except:
    
    print('Does not exist ')
    

  return render(request, 'greener/sponsorship.html');

def announcement_delete(request, id):
  try:
    announce = Announcement.objects.get(id=id)
    announce.delete()
  except:
    
    print('Does not exist ')
    

  return render(request, 'greener/announcement.html');

def announcement(request):
  announcement = Announcement.objects.all()
  context = {'announcements': announcement}
  
  return render(request, 'greener/announcement.html', context);
