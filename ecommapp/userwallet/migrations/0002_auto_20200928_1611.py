# Generated by Django 3.0.8 on 2020-09-28 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userwallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='account_number',
            field=models.IntegerField(default='7712411609'),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userwallet', to=settings.AUTH_USER_MODEL),
        ),
    ]
