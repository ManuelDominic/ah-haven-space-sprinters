# Generated by Django 2.1.7 on 2019-04-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_on_text',
            field=models.TextField(default=None, null=True),
        ),
    ]
