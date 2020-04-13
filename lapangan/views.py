from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .models import Lapangan, Waktu, Booking
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core import serializers


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lapangan:index')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return render(request, 'lapangan/login.html')

    context = {}
    return render(request, 'lapangan/login.html')


def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah dibuat, silakan login.')
            return redirect('lapangan:login')

    context = {'form': form}
    return render(request, 'lapangan/register.html', context)


def Logout(request):
    logout(request)
    return render(request, 'lapangan/index.html')


class IndexView(generic.ListView):
    template_name = 'lapangan/index.html'
    context_object_name = 'latest_lapangan_list'

    def get_queryset(self):
        return Lapangan.objects.all()


def Detail(request, lapangan_id):
    lapangan = get_object_or_404(Lapangan, pk=lapangan_id)
    jadwal = Booking
    context = {
        'lapangan': lapangan,
        'jadwal': jadwal,
    }
    return render(request, 'lapangan/detail.html', context)


def GetJadwal(request):
    atanggal = request.GET.get('tgl', None)    
    jadwal = Booking.objects.all().values().filter(lapangan_id=1, tanggal=atanggal)
    list_jadwal = list(jadwal)

    data = {
        'req': atanggal,
        'jad': jadwal,
    }
    return JsonResponse(list_jadwal, safe=False)

def GetWaktu(request):
    waktu = Waktu.objects.all().values()
    list_waktu = list(waktu)
    data = {
        'waktu': waktu
    }
    return JsonResponse(list_waktu, safe=False)
    