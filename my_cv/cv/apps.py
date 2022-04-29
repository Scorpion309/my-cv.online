from django.apps import AppConfig


class CvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cv'

    def ready(self):
        from cv.signals import create_user_profile
        from django.contrib.auth.models import User
        from django.db.models.signals import post_save

        post_save.connect(create_user_profile, sender=User)
