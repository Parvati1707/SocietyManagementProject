# Generated by Django 4.2.4 on 2024-01-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0072_alter_add_house_house_type_alter_add_house_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('3bhk', '3BHK'), ('2bhk', '2BHK'), ('1bhk', '1BHK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='add_society',
            name='Society_Image',
            field=models.FileField(default='Avatar.png', upload_to='Society_Images/'),
        ),
    ]
