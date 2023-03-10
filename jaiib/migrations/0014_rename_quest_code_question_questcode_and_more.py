# Generated by Django 4.1.7 on 2023-03-04 18:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0013_remove_profile_user_delete_brainjaiib_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quest_code',
            new_name='questcode',
        ),
        migrations.RemoveField(
            model_name='question',
            name='course_code',
        ),
        migrations.RemoveField(
            model_name='question',
            name='difficulty_code',
        ),
        migrations.RemoveField(
            model_name='question',
            name='sub_code',
        ),
        migrations.AddField(
            model_name='question',
            name='subcode',
            field=models.IntegerField(default=1, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{4}$')]),
            preserve_default=False,
        ),
    ]
