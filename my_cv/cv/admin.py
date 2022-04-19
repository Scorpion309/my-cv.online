from django.contrib import admin

from .models import Person, Education, Experience, Languages, StudyPlaces, Cities, Companies, Countries, Skills, \
    Positions


# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'first_name', 'last_name', 'general_skill', 'position', 'country', 'city', 'email')


@admin.register(Countries)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('country_name',)


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country')


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


@admin.register(StudyPlaces)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('study_place_name',)


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('language', 'language_level')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('course', 'study_place')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'company', 'city', 'position')


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill',)


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('position',)
