# Generated by Django 3.2 on 2021-04-09 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panchayat', '0004_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='name',
            new_name='staffname',
        ),
    ]
