from django.db import models
from django.contrib.auth.models import User


class Lapangan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.CharField()


class Harga(models.Model):
    harga = models.CharField(max_length=50)


class Waktu(models.Model):
    harga = models.ForeignKey(Harga, on_delete=models.CASCADE)
    waktu = models.DateTimeField('waku main')


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    waktu = models.ForeignKey(Waktu, on_delete=models.CASCADE)