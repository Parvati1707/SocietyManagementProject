# Generated by Django 4.2.4 on 2024-01-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0018_alter_add_house_block_no_alter_add_house_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_society',
            name='City',
            field=models.CharField(default='', max_length=100),
        ),
    ]
