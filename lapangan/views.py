from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Lapangan, Waktu


class IndexView(generic.ListView):
    template_name = 'lapangan/index.html'
    context_object_name = 'latest_lapangan_list'

    def get_queryset(self):
        return Lapangan.objects.all()


class DetailView(generic.DetailView):
    model = Lapangan
    template_name = 'lapangan/detail.html'
