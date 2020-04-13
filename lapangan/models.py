from django.db import models
from django.contrib.auth.models import User


class Rumput(models.Model):
    jenis_rumput = models.CharField(max_length=100)

    def __str__(self):
        return self.jenis_rumput


class Lapangan(models.Model):
    nama = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='images/lapangan/', max_length=None,
                               default='images/lapangan/no_img.jpeg', blank=True)
    jenis_rumput = models.ForeignKey(Rumput, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama


class Harga(models.Model):
    harga = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.harga


class Waktu(models.Model):
    harga = models.ForeignKey(Harga, on_delete=models.CASCADE)
    waktu = models.CharField(max_length=100)

    def __str__(self):
        return self.waktu


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    waktu = models.ForeignKey(Waktu, on_delete=models.CASCADE)
    tanggal = models.DateTimeField(auto_now_add=True)
