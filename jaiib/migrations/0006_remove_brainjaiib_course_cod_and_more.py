# Generated by Django 4.1.7 on 2023-02-21 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0005_remove_profile_course_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brainjaiib',
            name='course_cod',
        ),
        migrations.RemoveField(
            model_name='brainjaiib',
            name='overall_running_average',
        ),
        migrations.AddField(
            model_name='brainjaiib',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brains', to='jaiib.profile'),
        ),
    ]
