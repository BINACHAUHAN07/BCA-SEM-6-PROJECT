# Generated by Django 4.1.3 on 2022-12-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
    ]
