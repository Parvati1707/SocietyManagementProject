# Generated by Django 4.2.4 on 2024-01-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0038_alter_add_house_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('1bhk', '1BHK'), ('3bhk', '3BHK'), ('2bhk', '2BHK')], max_length=50),
        ),
    ]
