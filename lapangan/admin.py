from django.contrib import admin

from .models import Lapangan


class LapanganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi')


admin.site.register(Lapangan, LapanganAdmin)
