# Generated by Django 4.2.4 on 2024-02-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0081_rename_society_security_registration_society_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='security_registration',
            name='Society_Name',
        ),
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('3bhk', '3BHK'), ('1bhk', '1BHK'), ('2bhk', '2BHK')], max_length=50),
        ),
    ]
