# Generated by Django 4.0.2 on 2022-02-22 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_registered',
        ),
    ]