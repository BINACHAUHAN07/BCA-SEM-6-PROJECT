# Generated by Django 4.1.3 on 2023-02-11 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
