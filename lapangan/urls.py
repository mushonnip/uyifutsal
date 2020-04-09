from django.urls import path
from . import views

app_name = 'lapangan'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:lapangan_id>/', views.Detail, name='detail'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.Register, name='register'),

]
