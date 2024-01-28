# Generated by Django 4.2.4 on 2024-01-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0071_alter_add_house_house_type_alter_add_house_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('2bhk', '2BHK'), ('3bhk', '3BHK'), ('1bhk', '1BHK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='add_house',
            name='Image',
            field=models.ImageField(upload_to='static/Society_images'),
        ),
        migrations.AlterField(
            model_name='add_society',
            name='Society_Image',
            field=models.ImageField(upload_to='static/Society_images'),
        ),
    ]
