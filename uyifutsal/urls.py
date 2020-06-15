from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include('bookings.urls')),
    path("", include('django.contrib.auth.urls')),
    path('jet_api/', include('jet_django.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls, name='admin'),
    path('sadmin/', include('sadmin.urls')),

]