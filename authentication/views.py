from authentication.forms import CustomLoginForm
from django.shortcuts import render, HttpResponseRedirect, reverse
# from helpers.funcs import form_errors_decoder
from .forms import CustomLoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
  context = {}
  if request.method == 'POST':
    form = CustomLoginForm(request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
      # print()
      if user.is_staff == False:
        user = login(request,user)
        
        return HttpResponseRedirect(reverse('host:index'))
      
      else:
        user = login(request,user)
      
        return HttpResponseRedirect(reverse('greener:index'))
      # user = authenticate()
    context['errs'] = form.errors
  return render(request, 'authentication/index.html', context)


def signOut(request):
  try:
    del request.session['sponsorship']
    del request.session['announcement']
  except:
    print('SignOut delete session')
  logout(request)
  return HttpResponseRedirect(reverse('authentication:sign_in'))