# Generated by Django 3.0.5 on 2020-04-13 19:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lapangan', '0002_auto_20200413_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='kode_booking',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]