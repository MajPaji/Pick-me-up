# Generated by Django 3.1.7 on 2021-03-16 05:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0005_auto_20210316_0550'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileInfo',
            new_name='UserProfile',
        ),
    ]