# Generated by Django 4.2.4 on 2024-01-17 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0060_event_type_alter_add_house_house_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='society_event',
            old_name='Event_Name',
            new_name='Event_Type',
        ),
    ]