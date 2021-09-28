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
      print(user)
      if user is not None:
        user = login(request,user)
        
        return HttpResponseRedirect(reverse('greener:index'))
      # user = authenticate()
    context['errs'] = form.errors
  return render(request, 'authentication/index.html', context)
