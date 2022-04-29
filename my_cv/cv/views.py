import datetime

from django.conf import settings
from django.db.models import Prefetch
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, reverse

from .models import Person, ExperiencePeriod, EducationPeriod


# Create your views here.

def index(request):
    return redirect(reverse("cv:get_my_cv", args=("Scorpion",)))


def get_cv(request, username):
    user = Person.objects.prefetch_related(
        'skills',
        'languages',
        Prefetch('work_experience',
                 queryset=ExperiencePeriod.objects.select_related('experience').all().order_by('-start_work_date')),
        Prefetch('education', queryset=EducationPeriod.objects.all().order_by('-start_study_date'))
    ).get(user_name=username)

    skills = user.skills.filter()
    languages = user.languages.filter()
    work_experience = user.work_experience.filter()
    education_periods = user.education.filter()

    if user:
        return render(request, "cv/cv.html", {
            'user': user,
            'my_photo': f'{settings.STATIC_URL}cv/I_am.jpeg',
            'cv': f'{settings.STATIC_URL}cv/my_cv.docx',
            'skills': skills,
            'languages': languages,
            'work_experience': work_experience,
            'education_periods': education_periods,
            'age': round((datetime.date.today() - user.birthday).days / 365),
        })
    else:
        return HttpResponseNotFound()
