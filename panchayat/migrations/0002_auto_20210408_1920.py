# Generated by Django 3.2 on 2021-04-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchayat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userreg',
            name='cpass',
        ),
        migrations.RemoveField(
            model_name='userreg',
            name='password',
        ),
    ]
