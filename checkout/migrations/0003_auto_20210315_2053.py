# Generated by Django 3.1.7 on 2021-03-15 20:53

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210315_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]