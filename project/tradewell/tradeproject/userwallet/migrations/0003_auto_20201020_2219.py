# Generated by Django 3.1.2 on 2020-10-20 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0002_auto_20201020_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='user_account_number',
            field=models.IntegerField(default='7712312154'),
        ),
    ]
