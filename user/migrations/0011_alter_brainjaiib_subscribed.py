# Generated by Django 4.1.7 on 2023-03-02 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_brainjaiib_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brainjaiib',
            name='subscribed',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProfileB', to='user.profile'),
        ),
    ]
