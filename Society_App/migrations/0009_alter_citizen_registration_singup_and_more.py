# Generated by Django 4.2.4 on 2024-01-06 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0008_alter_citizen_registration_singup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen_registration',
            name='singup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.singup'),
        ),
        migrations.AlterField(
            model_name='singup',
            name='Username',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
