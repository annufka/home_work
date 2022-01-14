from django.contrib.auth.models import User
from django.db import models
from pytz import unicode


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    summ = models.IntegerField(default=0)
    code = models.IntegerField(default=0)

    def __str__(self):
        return unicode(str(self.summ))

class Music(models.Model):
    singer = models.CharField(max_length=50)
    song = models.CharField(max_length=100, null=True, blank=True)
    data_type = models.DateField(blank=True, null=True)

    def __str__(self):
        return unicode(str(self.singer)+'-'+str(self.song))