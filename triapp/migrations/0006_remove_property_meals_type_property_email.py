# Generated by Django 4.2.1 on 2023-05-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triapp', '0005_property_area_property_locationstate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='meals_type',
        ),
        migrations.AddField(
            model_name='property',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
    ]
