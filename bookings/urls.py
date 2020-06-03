from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'bookings'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('detail/<int:field_id>/', views.Detail, name='detail'),
    path('get-time/', views.GetTime, name='get_time'),
    path('get-schedule/', views.GetSchedule, name='get_schedule'),
    path('get-sch/', views.GetSch, name='get_sch'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
