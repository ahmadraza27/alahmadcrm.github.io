# Generated by Django 4.2.3 on 2023-07-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stock_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='box_capacity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock_in',
            name='box_capacity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock_out',
            name='box_capacity',
            field=models.FloatField(),
        ),
    ]
