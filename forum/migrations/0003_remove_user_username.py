# Generated by Django 3.2.2 on 2021-05-16 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]