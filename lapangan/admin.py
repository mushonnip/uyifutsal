from django.contrib import admin

from .models import Lapangan, Rumput, Waktu, Harga, Booking, Profile


class LapanganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_rumput')


class HargaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga')

class WaktuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'waktu', 'harga')

class BookingAdmin(admin.ModelAdmin):
    # list_display = ('kode_booking', 'user', 'waktu', 'tanggal')
    list_display = ('kode_booking', 'Waktu', 'user', 'tanggal')

    def Waktu(self, obj):
        return ", \n".join([str(p) for p in obj.waktu.all()])

admin.site.register(Lapangan, LapanganAdmin)
admin.site.register(Rumput)
admin.site.register(Waktu, WaktuAdmin)
admin.site.register(Harga, HargaAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Profile)