from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cv/<str:username>', views.get_cv, name="get_my_cv")
]
