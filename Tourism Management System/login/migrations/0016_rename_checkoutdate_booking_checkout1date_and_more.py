# Generated by Django 4.1.3 on 2023-02-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_booking_checkoutdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='checkoutdate',
            new_name='checkout1date',
        ),
        migrations.AddField(
            model_name='booking',
            name='packageid',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]