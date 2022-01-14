from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pytz import unicode


class Pasport(models.Model):

    status_choice = (("m", "married"), ("n", "not married"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    registration = models.TextField()
    status = models.CharField(max_length=15, choices=status_choice)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return unicode(str(self.user))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Pasport.objects.create(user=instance)