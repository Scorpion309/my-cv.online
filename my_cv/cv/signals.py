from cv.models import Person

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(username=instance)
