# Generated by Django 4.2.4 on 2024-01-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0065_remove_singup_email_citizen_registration_email_and_more'),
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