# Generated by Django 4.2.4 on 2024-01-17 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0044_singup_is_admin_alter_add_house_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('1bhk', '1BHK'), ('2bhk', '2BHK'), ('3bhk', '3BHK')], max_length=50),
        ),
        migrations.CreateModel(
            name='Sell_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entry_Date', models.DateField(auto_created=True, default='2018-12-12')),
                ('Sell_Price', models.FloatField(default='', max_length=10)),
                ('Citizen_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.singup')),
                ('House_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.add_house')),
                ('Society_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.add_society')),
            ],
        ),
        migrations.CreateModel(
            name='Rent_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entry_Date', models.DateField(auto_created=True, default='2018-12-12')),
                ('Rent_Price', models.FloatField(default='', max_length=20)),
                ('Citizen_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.singup')),
                ('House_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.add_house')),
                ('Society_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Society_App.add_society')),
            ],
        ),
    ]
