# Generated by Django 2.1.15 on 2020-04-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapangan', '0006_auto_20200421_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='kode_booking',
            field=models.CharField(default='F072F', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='point',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]