# Generated by Django 4.2.1 on 2023-05-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triapp', '0003_host_userdata_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='amenities',
            new_name='beds',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='description',
            new_name='instructions',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='area',
            new_name='number_of_bedrooms',
        ),
        migrations.RemoveField(
            model_name='property',
            name='images',
        ),
        migrations.RemoveField(
            model_name='property',
            name='length_of_stay',
        ),
        migrations.RemoveField(
            model_name='property',
            name='nearest_station_airport',
        ),
        migrations.RemoveField(
            model_name='property',
            name='nearest_station_bus',
        ),
        migrations.RemoveField(
            model_name='property',
            name='nearest_station_train',
        ),
        migrations.RemoveField(
            model_name='property',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='property',
            name='preferred_guest',
        ),
        migrations.RemoveField(
            model_name='property',
            name='rental_mode',
        ),
        migrations.RemoveField(
            model_name='property',
            name='sleeping_arrangement',
        ),
        migrations.RemoveField(
            model_name='property',
            name='type',
        ),
        migrations.RemoveField(
            model_name='property',
            name='washrooms',
        ),
        migrations.AddField(
            model_name='property',
            name='aadhar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='allowed_guest',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='apartment_size',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bathroom',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='cooking_cleaning_amenities',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='free_meals',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='general_amenities',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='gstin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='house_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='house_rules',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='landmark',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='languages',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='living_room',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='meals_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='no_of_separate_bathrooms',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='number_of_bathrooms',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='number_properties',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='other_amenities',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='other_spaces',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='outside_view',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='paid_meals',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='pan',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='parking',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='parking_spots',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='postal_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price_per_month',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price_per_night',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price_per_week',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_model',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='shared_spaces',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='property/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
