from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Lapangan, Waktu, Jadwal
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lapangan:index')
        else:
            messages.info(request, 'username or password incorrect')
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


# class DetailView(generic.DetailView):
#     model = Lapangan
#     template_name = 'lapangan/detail.html'


def Detail(request, lapangan_id):
    lapangan = get_object_or_404(Lapangan, pk=lapangan_id)
    jadwal = Jadwal
    context = {
        'lapangan': lapangan,
        'jadwal': jadwal,
    }
    return render(request, 'lapangan/detail.html', context)
