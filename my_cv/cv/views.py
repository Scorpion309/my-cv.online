from django.shortcuts import render, redirect, reverse
from .models import Person
from django.http import HttpResponseNotFound

# Create your views here.

def index(request):
    return redirect(reverse("get_my_cv", args=("Scorpion", )))

def get_cv(request, username):
    user = Person.objects.get(user_name=username)
    if user:
        return render(request, "cv.html", {'user': user})
    else:
        return HttpResponseNotFound()
