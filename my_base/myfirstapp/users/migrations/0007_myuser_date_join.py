# Generated by Django 3.0.8 on 2020-09-03 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200903_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='date_join',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
