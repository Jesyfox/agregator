# Generated by Django 2.2 on 2019-04-15 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_parser', '0002_auto_20190412_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]