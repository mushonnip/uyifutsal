import uuid, datetime
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    point = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

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
    kode_booking = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    # waktu = models.ForeignKey(Waktu, on_delete=models.CASCADE)
    waktu = models.ManyToManyField(Waktu)
    tanggal = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.kode_booking)
