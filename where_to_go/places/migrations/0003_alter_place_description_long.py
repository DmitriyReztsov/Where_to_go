# Generated by Django 4.1.1 on 2022-09-24 06:50

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0002_auto_20220923_1528"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
