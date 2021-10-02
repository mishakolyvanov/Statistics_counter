import datetime

from django.db import models


class Event(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    views = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=0)

