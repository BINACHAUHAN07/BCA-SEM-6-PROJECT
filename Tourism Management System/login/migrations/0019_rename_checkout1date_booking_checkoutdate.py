# Generated by Django 4.1.3 on 2023-02-17 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_booking_prise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='checkout1date',
            new_name='checkoutdate',
        ),
    ]