# Generated by Django 3.0.7 on 2020-06-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0015_auto_20200607_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_code',
            field=models.CharField(default='1ea-278', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.png', upload_to=''),
        ),
    ]
