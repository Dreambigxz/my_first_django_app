# Generated by Django 3.1 on 2020-09-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_myuser_date_join'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='verification_pin',
            field=models.CharField(default=67720, editable=False, max_length=10),
        ),
    ]