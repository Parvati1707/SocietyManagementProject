# Generated by Django 4.2.4 on 2024-01-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0066_remove_citizen_registration_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_society',
            old_name='NoHouse',
            new_name='No_Of_House',
        ),
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('1bhk', '1BHK'), ('3bhk', '3BHK'), ('2bhk', '2BHK')], max_length=50),
        ),
    ]