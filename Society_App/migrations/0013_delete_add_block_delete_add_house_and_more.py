# Generated by Django 4.2.4 on 2024-01-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0012_add_society_address_alter_add_society_society_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Add_Block',
        ),
        migrations.DeleteModel(
            name='Add_House',
        ),
        migrations.AlterField(
            model_name='add_society',
            name='Society_Image',
            field=models.ImageField(upload_to='static/Society_images'),
        ),
        migrations.AlterField(
            model_name='add_society',
            name='Society_Name',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
