# Generated by Django 4.1.3 on 2023-02-20 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_rename_listofplace_package_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='Prise',
            new_name='Price',
        ),
    ]