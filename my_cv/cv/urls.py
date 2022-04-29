from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'cv'

urlpatterns = [
                  path('', views.index, name="index"),
                  path('cv/<str:username>', views.get_cv, name="get_my_cv"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
