# Generated by Django 3.1 on 2020-10-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_auto_20201003_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='ratin',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
