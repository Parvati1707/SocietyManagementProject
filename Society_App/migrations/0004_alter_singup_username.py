# Generated by Django 4.2.4 on 2024-01-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0003_security_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singup',
            name='Username',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
