# Generated by Django 4.2.4 on 2024-01-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0028_alter_add_house_entry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('3bhk', '3BHK'), ('2bhk', '2BHK'), ('1bhk', '1BHK')], max_length=50),
        ),
    ]