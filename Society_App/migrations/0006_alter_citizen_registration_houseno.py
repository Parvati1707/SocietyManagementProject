# Generated by Django 4.2.4 on 2024-01-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0005_alter_citizen_registration_houseno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen_registration',
            name='HouseNo',
            field=models.CharField(default='', max_length=10),
        ),
    ]
