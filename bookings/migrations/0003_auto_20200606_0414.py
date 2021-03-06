# Generated by Django 3.0.6 on 2020-06-06 04:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20200606_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Lunas', 'Selesai'), ('Belum Lunas', 'Belum Selesai')], default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/media/avatar.png', upload_to=''),
        ),
    ]
