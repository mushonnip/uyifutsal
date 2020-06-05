from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Booking, Field, Time, Price
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CreateBookingForm


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'field_list'

    def get_queryset(self):
        return Field.objects.all()


def Detail(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    schedule = Booking

    if request.method == "POST":
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings:detail', field_id=field_id)
    else:
        form = CreateBookingForm()

    context = {
        'field': field,
        'schedule': schedule,
        'form': form
    }
    return render(request, 'detail.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('bookings:index')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return render(request, 'login.html')
        
    

    context = {}
    return render(request, 'login.html')


def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah dibuat, silakan login.')
            return redirect('bookings:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def Logout(request):
    logout(request)
    return render(request, 'index.html')


def GetTime(request):
    time = Time.objects.all().values()
    time_list = list(time)
    # data = {
    #     'time': time
    # }
    return JsonResponse(time_list, safe=False)


def GetSchedule(request):
    _date = request.GET.get('_date', None)
    _field_id = request.GET.get('_field_id', None)
    schedule = Booking.objects.all().values().filter(date=_date, field_id=_field_id)
    schedule_list = list(schedule)

    return JsonResponse(schedule_list, safe=False)

def GetSch(request):
    _date = request.GET.get('_date', None)
    _field_id = request.GET.get('_field_id', None)
    times = Time.objects.all().values()
    prices = Price.objects.all().values()
    # schedule = Booking.objects.all().values().filter(date=_date, field_id=_field_id)
    schedules = Booking.objects.all().filter(date=_date, field_id=_field_id)
    sch_lists = list(times)
    book_lists = list(schedules)
    price_lists = list(prices)

    lis = []
    for _ in schedules:
        _time = _.time.all()
        for t in _time:
            lis.append(t)
            

    for i, x in enumerate(sch_lists):
        for p in price_lists:
            if x['price_id'] == p['id']:
                sch_lists[i]['price'] = p['price']
                sch_lists[i]['point_required'] = p['point_required']
        for y in book_lists:
            # if y['time_id'] == x['id']:
            #     sch_lists[i]['status'] = 'booked'
            for a in lis:
                if x['time'] == a.time:
                    sch_lists[i]['status'] = 'booked'

            # if x['time'] == '10.00 - 11.00':
            #     sch_lists[i]['status'] = 'booked'
    
    
    return JsonResponse(sch_lists, safe=False)

def CreateBooking(request):
    form = CreateBookingForm()
    return render(request, 'detail.html', {'form':form})