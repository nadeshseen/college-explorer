# Generated by Django 3.2.7 on 2021-10-23 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='research_areas',
            field=models.CharField(default='', max_length=100),
        ),
    ]
