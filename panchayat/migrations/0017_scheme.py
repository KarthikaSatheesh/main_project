# Generated by Django 3.2 on 2021-04-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchayat', '0016_gramasabha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme', models.CharField(max_length=30)),
                ('requirements', models.CharField(max_length=30)),
            ],
        ),
    ]
