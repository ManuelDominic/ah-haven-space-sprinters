# Generated by Django 2.1.7 on 2019-04-25 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_commentnotification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentnotification',
            options={'ordering': ['created_at']},
        ),
    ]
