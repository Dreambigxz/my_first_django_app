# Generated by Django 3.0.8 on 2020-09-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0002_auto_20200928_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='account_number',
            field=models.IntegerField(default='7711630525'),
        ),
    ]
