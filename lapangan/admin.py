from django.contrib import admin

from .models import Lapangan, Rumput, Waktu, Harga, Jadwal, Booking


class LapanganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_rumput')


class HargaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga')


admin.site.register(Lapangan, LapanganAdmin)
admin.site.register(Rumput)
admin.site.register(Waktu)
admin.site.register(Harga, HargaAdmin)
admin.site.register(Jadwal)
admin.site.register(Booking)
