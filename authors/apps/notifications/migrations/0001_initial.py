# Generated by Django 2.1.7 on 2019-04-23 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_articlelikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email_sent', models.BooleanField(default=False)),
                ('classification', models.TextField(default='article')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('notified', models.ManyToManyField(related_name='notified', to=settings.AUTH_USER_MODEL)),
                ('read_by', models.ManyToManyField(related_name='read', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]