# Generated by Django 5.0.3 on 2024-03-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_userprofile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
