from django.urls import path
from django.conf import settings
from . import views

app_name = 'sadmin'
urlpatterns = [
    path("", views.Index, name="index"),
    path("users/", views.Users, name="users"),
    path("bookingan/", views.Bookingan, name="bookingan"),

    path("get-booking/", views.get_booking, name="get-booking"),
    path("update-booking/", views.update_bookng, name="update-booking"),
    path("get-users/", views.get_users, name="get-users"),
]
