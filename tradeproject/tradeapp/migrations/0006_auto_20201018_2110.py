# Generated by Django 3.1.2 on 2020-10-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0005_unpaid_user_amount_to_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid_user',
            name='recieved_amount',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=500000, null=True),
        ),
    ]
