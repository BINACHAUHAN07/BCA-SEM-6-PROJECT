# Generated by Django 4.1.3 on 2022-12-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
