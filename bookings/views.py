from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Booking, Field, Time, Price
from django.http import JsonResponse


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'field_list'

    def get_queryset(self):
        return Field.objects.all()


def Detail(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    schedule = Booking
    context = {
        'field': field,
        'schedule': schedule,
    }
    return render(request, 'detail.html', context)


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
    schedule = Booking.objects.all().values().filter(date=_date, field_id=_field_id)
    sch_lists = list(times)
    book_lists = list(schedule)
    price_lists = list(prices)

    for i, x in enumerate(sch_lists):
        for p in price_lists:
            if x['price_id'] == p['id']:
                sch_lists[i]['price'] = p['price']
        for y in book_lists:
            if y['time_id'] == x['id']:
                sch_lists[i]['status'] = 'booked'
    
    
    return JsonResponse(sch_lists, safe=False)