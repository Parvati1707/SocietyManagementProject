# Generated by Django 4.2.4 on 2024-02-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0083_alter_add_house_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('1bhk', '1BHK'), ('2bhk', '2BHK'), ('3bhk', '3BHK')], max_length=50),
        ),
    ]