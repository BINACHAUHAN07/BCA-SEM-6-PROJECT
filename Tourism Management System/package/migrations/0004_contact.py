# Generated by Django 4.1.3 on 2023-02-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=250)),
                ('Message', models.CharField(max_length=250)),
            ],
        ),
    ]