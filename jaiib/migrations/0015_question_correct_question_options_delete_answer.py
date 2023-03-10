# Generated by Django 4.1.7 on 2023-03-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0014_rename_quest_code_question_questcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
