# Generated by Django 3.2 on 2022-09-23 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20220923_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='imgs',
        ),
    ]