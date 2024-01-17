# Generated by Django 4.2.4 on 2024-01-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0059_alter_add_house_house_type_alter_notice_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('2bhk', '2BHK'), ('1bhk', '1BHK'), ('3bhk', '3BHK')], max_length=50),
        ),
    ]
