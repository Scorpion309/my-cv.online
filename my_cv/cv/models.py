import os
import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
LANGUAGE_LEVELS = (
    ("A1", "A1"),
    ("A2", "A2"),
    ("B1", "B1"),
    ("B2", "B2"),
    ("C1", "C1"),
    ("C2", "C2"),
)


class Positions(models.Model):
    position = models.CharField(
        _('Position'),
        max_length=32,
        unique=True,
        help_text=_("Обязательное поле. Длина должна быть не более 32 символов!"),
        error_messages={"unique": _("Такая должность уже сужествует в базе данных!")},
    )

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')


class Skills(models.Model):
    skill = models.CharField(
        _('Skill'),
        max_length=32,
        unique=True,
        help_text=_("Обязательное поле. Длина должна быть не более 32 символов!"),
        error_messages={"unique": _("Такой 'skill' уже сужествует в базе данных!")},
    )

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')


class Languages(models.Model):
    language = models.CharField(
        _('Language'),
        max_length=32,
        help_text=_("Обязательное поле. Длина должна быть не более 32 символов!"),
    )

    language_level = models.CharField(
        _('Language_level'),
        max_length=2,
        choices=LANGUAGE_LEVELS,
    )

    def __str__(self):
        return f"{self.language} {self.language_level}"

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


class Companies(models.Model):
    company_name = models.CharField(
        _('Company'),
        max_length=32,
        unique=True,
        help_text=_("Обязательное поле. Длина должна быть не более 32 символов!"),
        error_messages={"unique": _("Такая компания уже сужествует в базе данных!")},
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class Countries(models.Model):
    country_name = models.CharField(
        _('Country'),
        max_length=32,
        unique=True,
        help_text=_("Обязательное поле. Длина должна быть не более 32 символов!"),
        error_messages={"unique": _("Такая страна уже сужествует в базе данных!")},
    )

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Cities(models.Model):
    city_name = models.CharField(
        _('City'),
        max_length=32,
        unique=True,
        help_text=_("Обязательное поле. Длина должна быть не более 32 символов!"),
        error_messages={"unique": _("Такой город уже сужествует в базе данных!")},
    )
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class Experience(models.Model):
    project_name = models.CharField(
        _('Project'),
        max_length=32,
        help_text=_("Обязательное поле. Длина должна быть не более 32 символов!"),
    )

    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f" '{self.project_name}', {self.company}, {self.city}"

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experience')


class ExperiencePeriod(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, null=True, on_delete=models.SET_NULL)
    start_work_date = models.DateField(_('Start of work'), blank=True, null=True)
    end_work_date = models.DateField(_('End of work'), blank=True, null=True)
    about_project = models.TextField(_('Information'), blank=True, null=True)

    def __str__(self):
        return f" '{self.experience} - {self.position} from {self.start_work_date} to {self.end_work_date}"

    class Meta:
        verbose_name = _('ExperiencePeriod')
        verbose_name_plural = _('ExperiencePeriod')


class StudyPlaces(models.Model):
    study_place_name = models.CharField(
        _('Study place'),
        unique=True,
        max_length=100,
        help_text=_("Обязательное поле. Длина должна быть не более 100 символов!"),
    )

    def __str__(self):
        return self.study_place_name

    class Meta:
        verbose_name = _('Study_place')
        verbose_name_plural = _('Study_places')


class Education(models.Model):
    course = models.CharField(
        _('Course'),
        max_length=100,
        unique=True,
        help_text=_("Обязательное поле. Длина должна быть не более 100 символов!"),
        error_messages={"unique": _("Такой курс уже существует!")},
    )

    study_place = models.ForeignKey(StudyPlaces, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.study_place}, '{self.course}'"

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Education')


class EducationPeriod(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    start_study_date = models.DateField(_('Start of education'), blank=True, null=True)
    end_study_date = models.DateField(_('End of education'), blank=True, null=True)
    about_education = models.TextField(_('Information'), blank=True, null=True)

    def __str__(self):
        return f"{self.education}, from {self.start_study_date} to {self.end_study_date}"

    class Meta:
        verbose_name = _('EducationPeriod')
        verbose_name_plural = _('EducationPeriod')


class Person(models.Model):

    def get_path_to_save_photo(self, filename):
        extension = filename.split('.')[-1]
        return os.path.join('photos/', f'{uuid.uuid4()}.{extension}')

    first_name = models.CharField(
        _('First name'),
        max_length=50,
        help_text=_(f"Обязательное поле. Длина должна быть не более 50 символов!"),
    )

    last_name = models.CharField(
        _('Last name'),
        max_length=50,
        help_text=_(f"Обязательное поле. Длина должна быть не более 50 символов!"),
    )

    user_name = models.CharField(
        _('Login'),
        max_length=50,
        unique=True,
        help_text=_(f"Обязательное поле. Длина должна быть не более 50 символов!"),
        error_messages={"unique": _("Пользователь с таким логином уже существует в нашем списке пользователей."
                                    " Пожалуйста, выберите другое имя!")},
    )
    photo = models.ImageField(_('Photo'), null=True, upload_to=get_path_to_save_photo)
    country = models.ForeignKey(Countries, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(_('E-mail'))
    phone = models.CharField(
        _('Telephone number'),
        max_length=13,
        help_text=_(f"Обязательное поле. Длина должна быть не более 13 символов!"),
    )

    linkedin = models.CharField(
        _('Linkedin profile'),
        max_length=70,
        help_text=_(f"Обязательное поле. Длина должна быть не более 70 символов!"),
    )

    github = models.CharField(
        _('Github profile'),
        max_length=50,
        help_text=_(f"Обязательное поле. Длина должна быть не более 50 символов!"),
    )

    filing_date = models.DateField(
        _('Filing date'),
    )

    position = models.ForeignKey(Positions, blank=True, null=True, on_delete=models.SET_NULL)
    general_skill = models.ForeignKey(Skills, blank=True, null=True, on_delete=models.SET_NULL)

    salary = models.IntegerField(
        _('Salary'),
        default=0,
        validators=[MinValueValidator(0)],
    )

    skills = models.ManyToManyField(Skills, blank=True, related_name='all_skills')
    languages = models.ManyToManyField(Languages, blank=True)

    work_experience = models.ManyToManyField(ExperiencePeriod, blank=True)

    education = models.ManyToManyField(EducationPeriod, blank=True)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return self.user_name
