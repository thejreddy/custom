# Generated by Django 4.1.7 on 2023-02-25 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0012_alter_brainjaiib_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='brainjaiib',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
