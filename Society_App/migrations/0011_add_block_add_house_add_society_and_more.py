# Generated by Django 4.2.4 on 2024-01-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0010_remove_citizen_registration_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Add_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Add_Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entry_Date', models.DateField(auto_created=True, default='1990/23/12')),
                ('Society_Name', models.TextField(default='', max_length=50)),
                ('City', models.CharField(default='', max_length=50)),
                ('PinCode', models.IntegerField(default='')),
                ('NoHouse', models.IntegerField(default='')),
                ('Society_Image', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.AlterField(
            model_name='citizen_registration',
            name='Address',
            field=models.TextField(default='', max_length=40),
        ),
    ]
