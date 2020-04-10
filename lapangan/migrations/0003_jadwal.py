# Generated by Django 3.0.5 on 2020-04-05 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lapangan', '0002_auto_20200404_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('lapangan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapangan.Lapangan')),
                ('waktu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapangan.Waktu')),
            ],
        ),
    ]