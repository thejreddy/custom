# Generated by Django 4.1.7 on 2023-02-22 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaiib', '0007_alter_brainjaiib_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brainjaiib',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jeans', to='jaiib.profile'),
        ),
    ]
