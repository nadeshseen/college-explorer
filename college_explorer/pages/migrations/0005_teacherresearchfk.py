# Generated by Django 3.2.7 on 2021-10-24 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_teacher_research_areas'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherResearchFK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_area', models.CharField(default='', max_length=100)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.teacher')),
            ],
        ),
    ]