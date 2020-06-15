from django.urls import path
from django.conf import settings
from . import views

app_name = 'sadmin'
urlpatterns = [
    path("", views.Index, name="index"),
    path("jadwal/", views.Jadwal, name="jadwal"),

    path("get-booking/", views.get_booking, name="get-booking"),
    path("get-user/", views.get_user, name="get-user"),
]
