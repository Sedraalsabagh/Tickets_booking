# Generated by Django 5.0.3 on 2024-03-25 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_flight_id_booking_flight_alter_booking_status'),
        ('flights', '0013_alter_flight_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='flight',
        ),
        migrations.AddField(
            model_name='booking',
            name='outbound_flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outbound_bookings', to='flights.flight'),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='return_bookings', to='flights.flight'),
        ),
        migrations.AddField(
            model_name='booking',
            name='trip_type',
            field=models.CharField(choices=[('OW', 'One Way'), ('RT', 'Round Trip')], default='OW', max_length=2),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('CNL', 'Canceled'), ('PPD', 'Postponed'), ('CMP', 'Completed')], default='CMP', max_length=3),
        ),
    ]
