# Generated by Django 2.1.7 on 2019-04-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='app_notification_enabled',
            field=models.BooleanField(default=True),
        ),
    ]