import json, uuid
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Booking, Field, Time, Price
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CreateBookingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'field_list'

    def get_queryset(self):
        return Field.objects.all()

def update_profile(request, user_id, new_point):
    user = User.objects.get(pk=user_id)
    user.profile.point = new_point
    user.save()
    

@login_required
def add_booking(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    book = Booking()
    if request.is_ajax() and request.POST:
        book_code = uuid.uuid1().hex[:3] + '-' + uuid.uuid4().hex[:3]
        book.booking_code = book_code.upper()
        book.field = Field.objects.get(pk=field_id)
        book.date  = request.POST.get('date')
        book.user = request.user
        times = json.loads(request.POST.get('time'))
        # user = request.user.id
        # user.profile.point = new_point
        # user.save()
        book.save()
        
        for i in times:
            time_id = i.get('id')
            book.time.add(time_id)

        data = {'message': book.booking_code}

        context = {
            'field': field, 
        }
        # return redirect(request, 'detail.html', context)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404



def Detail(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    schedule = Booking

    context = {
        'field': field,
        'schedule': schedule,
    }

    return render(request, 'detail.html', context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('bookings:index')
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
    if request.user.is_authenticated:
        return redirect('bookings:index')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah dibuat, silakan login.')
            return redirect('bookings:login')

    context = {'form': form}
    return render(request, 'register.html', context)

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
            for a in lis:
                if x['time'] == a.time:
                    sch_lists[i]['status'] = 'booked'

    return JsonResponse(sch_lists, safe=False)

def CreateBooking(request):
    form = CreateBookingForm()
    return render(request, 'detail.html', {'form':form})

