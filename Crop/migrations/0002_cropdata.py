# Generated by Django 3.1.7 on 2021-03-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField()),
                ('ha_yield', models.IntegerField()),
                ('avg_rainfall_mm', models.IntegerField()),
                ('pesticides_tonnes', models.IntegerField()),
                ('avg_tem', models.IntegerField()),
            ],
        ),
    ]
