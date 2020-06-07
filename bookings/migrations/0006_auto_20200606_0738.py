# Generated by Django 3.0.6 on 2020-06-06 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20200606_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Lunas', 'Selesai'), ('Belum Lunas', 'Belum Selesai')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_code',
            field=models.CharField(default='bf4-1d3', editable=False, max_length=50),
        ),
        migrations.DeleteModel(
            name='BookingTime',
        ),
    ]
