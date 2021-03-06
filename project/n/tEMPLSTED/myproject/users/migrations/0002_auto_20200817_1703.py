# Generated by Django 3.0.8 on 2020-08-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.IntegerField(default=123),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='User Name'),
        ),
    ]
