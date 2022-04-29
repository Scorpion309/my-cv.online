from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect

from .forms import LoginForm


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             user = authenticate(
#                 username=clean_data['username'],
#                 password=clean_data['password'],
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect(reverse("cv:index"))
#                 else:
#                     return HttpResponse('This user is not active!')
#             else:
#                 return HttpResponse('Invalid username/password!')
#     else:
#         form = LoginForm()
#         return render(request, 'users/login.html', {'form': form})
