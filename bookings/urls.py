from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'bookings'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('detail/<int:field_id>/', views.Detail, name='detail'),
    path("dashboard/", views.Dashboard, name="dashboard"),

    # path('logout/', views.Logout, name='logout'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('xadmin/', views.Admin, name='sadmin'),

    path("create-booking/<int:field_id>/", views.add_booking, name="create_booking"),
    path("update-profile/<int:user_id>/<int:new_point>/", views.update_profile, name="update_profile"),
    path('get-sch/', views.GetSch, name='get_sch'),
    path('get-point/', views.get_point, name='get_point'),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
