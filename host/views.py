from django.shortcuts import render
from greener.models import Program
# Create your views here.


def index(request):
  program = Program.objects.filter(host__user = request.user)
  context={'programs': program}
  return render(request, 'host/index.html', context)

def user_programs(request):
  # program = Program.objects.all()
  # context= {
  # 'programs': program
  # }
  
  return render(request, 'host/user_programs.html')


def announcements(request):

  program = Program.objects.filter(host__user = request.user)

  return render(request, 'host/user_announcements.html', context={'programs': program})


def sponsorships(request):
  return render(request, 'host/user_sponsorships.html')