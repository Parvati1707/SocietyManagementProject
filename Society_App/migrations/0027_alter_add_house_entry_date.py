# Generated by Django 4.2.4 on 2024-01-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0026_rename_society_add_house_society_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='Entry_Date',
            field=models.DateField(auto_created=True, default='2012-08-12'),
        ),
    ]
