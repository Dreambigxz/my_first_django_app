# Generated by Django 3.1 on 2020-09-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_myuser_verification_pin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='verification_pin',
        ),
        migrations.AddField(
            model_name='myuser',
            name='tokken',
            field=models.CharField(default=63046, max_length=10),
        ),
    ]
