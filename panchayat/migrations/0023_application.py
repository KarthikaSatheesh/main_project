# Generated by Django 3.2 on 2021-04-22 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchayat', '0022_userreg_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schemeid', models.CharField(max_length=30)),
                ('userid', models.CharField(max_length=30)),
                ('photo', models.FileField(upload_to='')),
                ('residencep', models.CharField(max_length=30)),
                ('idcardp', models.CharField(max_length=30)),
                ('taxp', models.CharField(max_length=30)),
                ('incomep', models.CharField(max_length=30)),
                ('castep', models.CharField(max_length=30)),
            ],
        ),
    ]
