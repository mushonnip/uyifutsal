import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    point = models.IntegerField(default=10, null=True, blank=True)
    avatar = models.ImageField(default='/media/avatar.png',height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Floor(models.Model):
    floor_type = models.CharField(max_length=50)

    def __str__(self):
        return self.floor_type

class Field(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(height_field=None, width_field=None, max_length=None)
    floor_type = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=0)
    price_name = models.CharField(max_length=50)
    point_required = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return "Rp. {} ({})".format(self.price, self.point_required)

class Time(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.time


STATUS_CHOICES = (
   ('Selesai', 'Selesai'),
   ('Belum Selesai', 'Belum Selesai')
)

class Booking(models.Model):
    booking_code = models.CharField(default=uuid.uuid1().hex[:3] + '-' + uuid.uuid4().hex[:3], max_length=50, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='Belum Selesai', choices=STATUS_CHOICES, max_length=100)
    

    # def get_time(self):
    #     return "\n".join([str(t) for t in self.time.all()])

    def __str__(self):
        return self.booking_code

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    rating = models.DecimalField(max_digits=5, decimal_places=0)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Schedule(models.Model):
    date = models.DateTimeField()
    
    def __str__(self):
        return "{}".format(self.date)