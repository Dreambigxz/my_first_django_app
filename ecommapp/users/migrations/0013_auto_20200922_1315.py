# Generated by Django 3.0.8 on 2020-09-22 12:15

from django.db import migrations, models
import users.myfunc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200922_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='tokken',
            field=models.CharField(default=users.myfunc.timestamp_Otp_Verification, max_length=20),
        ),
    ]
