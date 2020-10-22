# Generated by Django 3.1.2 on 2020-10-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0006_auto_20201018_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paid_user',
            old_name='completed',
            new_name='merged_completed',
        ),
        migrations.RenameField(
            model_name='unpaid_user',
            old_name='completed',
            new_name='merged_completed',
        ),
        migrations.RemoveField(
            model_name='paid_user',
            name='recieved_amount',
        ),
        migrations.AddField(
            model_name='paid_user',
            name='interest',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=500000),
        ),
        migrations.AddField(
            model_name='paid_user',
            name='merged_to_pay',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paid_user',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unpaid_user',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='paid_user',
            name='recieving_amount',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=500000, null=True),
        ),
    ]
