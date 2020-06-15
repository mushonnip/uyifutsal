import json
from django.http import Http404, HttpResponse
from django.shortcuts import render
from bookings.models import Booking, Time, Profile
from django.contrib.auth.models import User
from django.core import serializers
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect


def Index(request):
    bookings = Booking.objects.order_by('time')
    users = User.objects.all()
    context = {
        'bookings': bookings,
        'users': users,
    }
    return render(request, 'sadmin/index.html', context)


def Jadwal(request):
    bookings = Booking.objects.order_by('time')
    users = User.objects.all()
    context = {
        'bookings': bookings,
        'users': users,
    }
    return render(request, 'sadmin/jadwal.html', context)


def get_booking(request):
    bookings = Booking.objects.all().order_by('time')
    book_serialized = serializers.serialize('python', bookings)

    for x in book_serialized:
        x['fields']['avatar'] = Profile.objects.get(pk=x['fields']['user']).avatar.url
        x['fields']['user'] = User.objects.get(pk=x['fields']['user']).username
        x['fields']['time'] = Time.objects.get(pk=x['fields']['time']).time

    
    return JsonResponse(book_serialized, safe=False)


def get_user(request):
    user = get_object_or_404(User, pk=request.GET.get('id'))
    # user_serialized = serializers.serialize('python', user)
    data = {
        'username': user.username,
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
