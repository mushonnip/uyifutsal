from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('lapangan.urls')),
    path('admin/', admin.site.urls, name='admin'),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
