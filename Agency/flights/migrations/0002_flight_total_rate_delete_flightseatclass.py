# Generated by Django 5.0.3 on 2024-03-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='total_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='FlightSeatClass',
        ),
    ]