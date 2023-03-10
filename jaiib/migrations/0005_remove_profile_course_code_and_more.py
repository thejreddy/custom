# Generated by Django 4.1.7 on 2023-02-21 16:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0004_profile_delete_performanceanalyst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='course_code',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='overall_running_average',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_101_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_101_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_101_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_102_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_102_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_102_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_103_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_103_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_103_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_104_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_104_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_104_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_105_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_105_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_105_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_106_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_106_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_106_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_107_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_107_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_107_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_108_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_108_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_108_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_109_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_109_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_109_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_110_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_110_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_110_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_111_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_111_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_111_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_112_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_112_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_112_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_113_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_113_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_113_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_114_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_114_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_114_3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_115_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_115_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sub_code_score_115_3',
        ),
        migrations.AddField(
            model_name='profile',
            name='course_cod',
            field=models.IntegerField(null=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 3', regex='^.{3}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='course_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='brainjaiib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_code_score_101_1', models.FloatField(null=True)),
                ('sub_code_score_101_2', models.FloatField(null=True)),
                ('sub_code_score_101_3', models.FloatField(null=True)),
                ('sub_code_score_102_1', models.FloatField(null=True)),
                ('sub_code_score_102_2', models.FloatField(null=True)),
                ('sub_code_score_102_3', models.FloatField(null=True)),
                ('sub_code_score_103_1', models.FloatField(null=True)),
                ('sub_code_score_103_2', models.FloatField(null=True)),
                ('sub_code_score_103_3', models.FloatField(null=True)),
                ('sub_code_score_104_1', models.FloatField(null=True)),
                ('sub_code_score_104_2', models.FloatField(null=True)),
                ('sub_code_score_104_3', models.FloatField(null=True)),
                ('sub_code_score_105_1', models.FloatField(null=True)),
                ('sub_code_score_105_2', models.FloatField(null=True)),
                ('sub_code_score_105_3', models.FloatField(null=True)),
                ('sub_code_score_106_1', models.FloatField(null=True)),
                ('sub_code_score_106_2', models.FloatField(null=True)),
                ('sub_code_score_106_3', models.FloatField(null=True)),
                ('sub_code_score_107_1', models.FloatField(null=True)),
                ('sub_code_score_107_2', models.FloatField(null=True)),
                ('sub_code_score_107_3', models.FloatField(null=True)),
                ('sub_code_score_108_1', models.FloatField(null=True)),
                ('sub_code_score_108_2', models.FloatField(null=True)),
                ('sub_code_score_108_3', models.FloatField(null=True)),
                ('sub_code_score_109_1', models.FloatField(null=True)),
                ('sub_code_score_109_2', models.FloatField(null=True)),
                ('sub_code_score_109_3', models.FloatField(null=True)),
                ('sub_code_score_110_1', models.FloatField(null=True)),
                ('sub_code_score_110_2', models.FloatField(null=True)),
                ('sub_code_score_110_3', models.FloatField(null=True)),
                ('sub_code_score_111_1', models.FloatField(null=True)),
                ('sub_code_score_111_2', models.FloatField(null=True)),
                ('sub_code_score_111_3', models.FloatField(null=True)),
                ('sub_code_score_112_1', models.FloatField(null=True)),
                ('sub_code_score_112_2', models.FloatField(null=True)),
                ('sub_code_score_112_3', models.FloatField(null=True)),
                ('sub_code_score_113_1', models.FloatField(null=True)),
                ('sub_code_score_113_2', models.FloatField(null=True)),
                ('sub_code_score_113_3', models.FloatField(null=True)),
                ('sub_code_score_114_1', models.FloatField(null=True)),
                ('sub_code_score_114_2', models.FloatField(null=True)),
                ('sub_code_score_114_3', models.FloatField(null=True)),
                ('sub_code_score_115_1', models.FloatField(null=True)),
                ('sub_code_score_115_2', models.FloatField(null=True)),
                ('sub_code_score_115_3', models.FloatField(null=True)),
                ('overall_running_average', models.FloatField(null=True)),
                ('course_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaiib.profile')),
            ],
        ),
    ]
