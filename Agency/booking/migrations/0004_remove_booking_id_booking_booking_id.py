# Generated by Django 5.0.3 on 2024-03-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_booking_flight_booking_outbound_flight_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='id',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]