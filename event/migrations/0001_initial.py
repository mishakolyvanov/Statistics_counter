# Generated by Django 3.2.7 on 2021-10-02 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('views', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
