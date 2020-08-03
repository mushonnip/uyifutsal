import json
import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render
from bookings.models import Booking, Time, Profile
from django.contrib.auth.models import User
from django.core import serializers
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url='/login')
def Index(request):
    bookings = Booking.objects.order_by('time')
    users = User.objects.all()
    context = {
        'bookings': bookings,
        'users': users,
    }
    return render(request, 'sadmin/index.html', context)

@login_required(login_url='/login')
def Bookingan(request):
    bookings = Booking.objects.order_by('time')
    users = User.objects.all()
    context = {
        'bookings': bookings,
        'users': users,
    }
    return render(request, 'sadmin/bookingan.html', context)

@login_required(login_url='/login')
def Users(request):
    users = User.objects.all()
    context = {
        'users': users
    }

    return render(request, 'sadmin/users.html', context)

@login_required(login_url='/login')
@staff_member_required
def get_users(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    # users_serialized = serializers.serialize('python', users)
    profiles_serialized = serializers.serialize('python', profiles)
    

    for x in profiles_serialized:
        user = User.objects.get(pk=x['fields']['user'])
        x['fields']['username'] = user.username
        x['fields']['is_active'] = user.is_active
        x['fields']['avatar'] = Profile.objects.get(pk=x['fields']['user']).avatar.url

    return JsonResponse(profiles_serialized, safe=False)

@login_required(login_url='/login')
@staff_member_required
def get_booking(request):
    # date = datetime.datetime.now()
    # .filter(date=date.strftime("%Y-%m-%d"))
    bookings = Booking.objects.all().order_by('time')
    book_serialized = serializers.serialize('python', bookings)

    for x in book_serialized:
        x['fields']['avatar'] = Profile.objects.get(pk=x['fields']['user']).avatar.url
        x['fields']['user'] = User.objects.get(pk=x['fields']['user']).username
        x['fields']['time'] = Time.objects.get(pk=x['fields']['time']).time

    return JsonResponse(book_serialized, safe=False)

@login_required(login_url='/login')
@staff_member_required
def get_user(request):
    user = get_object_or_404(User, pk=request.GET.get('id'))
    data = {
        'username': user.username,
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

@login_required(login_url='/login')
@staff_member_required
def update_bookng(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Booking.objects.get(pk=request.POST.get('pk_id'))
            obj.status = request.POST['status']
            obj.save()
            return JsonResponse({'status': 'Success', 'msg': 'save successfully'})
        except Booking.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})
    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})
