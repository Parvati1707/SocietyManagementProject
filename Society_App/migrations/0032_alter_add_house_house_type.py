# Generated by Django 4.2.4 on 2024-01-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0031_arrange_meeting_alter_add_house_house_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrange_Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.DateField(auto_created=True, default='2018-12-12')),
                ('Meet_Agenda', models.TextField(default=True)),
                ('Meet_conclusion', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='add_house',
            name='House_Type',
            field=models.CharField(choices=[('3bhk', '3BHK'), ('2bhk', '2BHK'), ('1bhk', '1BHK')], max_length=50),
        ),
    ]
