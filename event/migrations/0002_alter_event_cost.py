# Generated by Django 3.2.7 on 2021-10-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
