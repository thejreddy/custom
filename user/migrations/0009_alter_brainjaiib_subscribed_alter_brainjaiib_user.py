# Generated by Django 4.1.7 on 2023-02-27 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_profile_subscribed1_profile_subscribed10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brainjaiib',
            name='subscribed',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProfileB', to='user.profile'),
        ),
        migrations.AlterField(
            model_name='brainjaiib',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserB', to='user.profile'),
        ),
    ]