# Generated by Django 3.2 on 2021-04-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchayat', '0019_staff_wardname'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='age',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='educationalqualification',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
