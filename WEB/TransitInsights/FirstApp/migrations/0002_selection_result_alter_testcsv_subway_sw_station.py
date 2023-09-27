# Generated by Django 4.2.4 on 2023-09-06 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Station_ON', models.TextField(max_length=100)),
                ('Station_OFF', models.TextField(max_length=100)),
                ('Get_Time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
            ],
        ),
        migrations.AlterField(
            model_name='testcsv_subway',
            name='SW_Station',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
