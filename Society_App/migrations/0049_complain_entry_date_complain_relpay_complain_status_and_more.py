# Generated by Django 4.2.4 on 2024-01-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0048_alter_add_house_house_no_alter_add_house_house_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='Entry_Date',
            field=models.DateField(auto_created=True, default='2018-12-12'),
        ),
        migrations.AddField(
            model_name='complain',
            name='Relpay',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='complain',
            name='Status',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('2bhk', '2BHK'), ('3bhk', '3BHK'), ('1bhk', '1BHK')], max_length=50),
        ),
        
    ]
