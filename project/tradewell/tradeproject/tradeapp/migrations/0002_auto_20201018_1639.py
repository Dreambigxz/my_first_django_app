# Generated by Django 3.1.2 on 2020-10-18 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid_user',
            name='date_paid',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
