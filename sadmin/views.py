from django.shortcuts import render

def Index(request):
    return render(request, 'sadmin/index.html')