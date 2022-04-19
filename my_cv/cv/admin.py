from django.contrib import admin
from .models import Person, Education, Experience, Languages, StudyPlaces, Cities, Companies, Countries

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'first_name', 'last_name', 'position', 'country', 'city', 'email')

@admin.register(Countries)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('country_name', )

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country')