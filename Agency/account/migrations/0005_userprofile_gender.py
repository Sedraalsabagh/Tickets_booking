# Generated by Django 5.0.3 on 2024-03-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customer_gender_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], null=True),
        ),
    ]
