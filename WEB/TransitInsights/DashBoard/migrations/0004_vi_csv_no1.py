# Generated by Django 4.2.5 on 2023-09-19 01:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0003_alter_csvforheatmaptest_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vi_CSV_NO1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MONTH', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('DAY', models.CharField(max_length=255)),
                ('STATION', models.CharField(max_length=255)),
                ('DIRECTION', models.CharField(max_length=255)),
                ('TIME_05', models.FloatField()),
                ('TIME_06', models.FloatField()),
                ('TIME_07', models.FloatField()),
                ('TIME_08', models.FloatField()),
                ('TIME_09', models.FloatField()),
                ('TIME_10', models.FloatField()),
                ('TIME_11', models.FloatField()),
                ('TIME_12', models.FloatField()),
                ('TIME_13', models.FloatField()),
                ('TIME_14', models.FloatField()),
                ('TIME_15', models.FloatField()),
                ('TIME_16', models.FloatField()),
                ('TIME_17', models.FloatField()),
                ('TIME_18', models.FloatField()),
                ('TIME_19', models.FloatField()),
                ('TIME_20', models.FloatField()),
                ('TIME_21', models.FloatField()),
                ('TIME_22', models.FloatField()),
                ('TIME_23', models.FloatField()),
                ('TIME_24', models.FloatField()),
            ],
        ),
    ]
