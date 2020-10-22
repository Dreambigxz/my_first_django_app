# Generated by Django 3.1 on 2020-09-11 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderitem',
        ),
        migrations.AddField(
            model_name='order',
            name='orderitem',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.orderitem'),
        ),
    ]