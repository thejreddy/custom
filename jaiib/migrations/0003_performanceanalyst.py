# Generated by Django 4.1.7 on 2023-02-20 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jaiib', '0002_remove_question_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='performanceanalyst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_code_score', models.FloatField()),
                ('overall_running_average', models.FloatField()),
                ('sub_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaiib.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
