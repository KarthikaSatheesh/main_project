# Generated by Django 3.2.3 on 2021-06-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchayat', '0028_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]
