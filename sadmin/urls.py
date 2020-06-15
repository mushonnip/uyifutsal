from django.urls import path
from django.conf import settings
from . import views

app_name = 'sadmin'
urlpatterns = [
    path("", views.Index, name="index")
]
