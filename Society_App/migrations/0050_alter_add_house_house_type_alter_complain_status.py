# Generated by Django 4.2.4 on 2024-01-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0049_complain_entry_date_complain_relpay_complain_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('2bhk', '2BHK'), ('1bhk', '1BHK'), ('3bhk', '3BHK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='complain',
            name='Status',
            field=models.CharField(default='', max_length=50),
        ),
    ]
