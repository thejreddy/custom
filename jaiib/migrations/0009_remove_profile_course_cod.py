# Generated by Django 4.1.7 on 2023-02-22 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0008_alter_brainjaiib_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='course_cod',
        ),
    ]