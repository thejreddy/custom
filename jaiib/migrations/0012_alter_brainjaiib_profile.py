# Generated by Django 4.1.7 on 2023-02-25 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0011_alter_brainjaiib_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brainjaiib',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jaiib.profile'),
        ),
    ]