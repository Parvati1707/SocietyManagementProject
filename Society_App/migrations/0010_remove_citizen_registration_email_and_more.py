# Generated by Django 4.2.4 on 2024-01-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0009_alter_citizen_registration_singup_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen_registration',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='committee_registration',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='security_registration',
            name='Email',
        ),
        migrations.AddField(
            model_name='singup',
            name='Email',
            field=models.EmailField(default='', max_length=30),
        ),
    ]
