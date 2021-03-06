# Generated by Django 3.0.8 on 2020-09-17 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0013_shippingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='myuser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state_of_origin',
            field=models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwayibom', 'Akwayibom'), ('Akwayibom', 'Akwayibom')], default='Abia', max_length=30),
        ),
    ]
