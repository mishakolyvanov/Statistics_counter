import datetime
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Event(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    views = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    clicks = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=0, validators=[MinValueValidator(Decimal('0.0'))])

