# Generated by Django 4.2.4 on 2024-01-17 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0058_notice_type_rename_fund_type_fund_type_fund_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('1bhk', '1BHK'), ('2bhk', '2BHK'), ('3bhk', '3BHK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.notice_type'),
        ),
    ]