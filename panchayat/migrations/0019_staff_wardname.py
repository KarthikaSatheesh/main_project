# Generated by Django 3.2 on 2021-04-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchayat', '0018_staff_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='wardname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
