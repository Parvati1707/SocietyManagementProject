# Generated by Django 4.2.4 on 2024-02-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0076_alter_guest_entry_citizen_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('1bhk', '1BHK'), ('2bhk', '2BHK'), ('3bhk', '3BHK')], max_length=50),
        ),
    ]
