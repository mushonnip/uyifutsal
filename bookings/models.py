import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    point = models.IntegerField(null=True, blank=True)
    
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

class Booking(models.Model):
    booking_code = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    time = models.ManyToManyField(Time)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_time(self):
        return "\n".join([str(t) for t in self.time.all()])

    def __str__(self):
        return self.booking_code


