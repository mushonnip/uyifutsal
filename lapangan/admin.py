from django.contrib import admin

from .models import Lapangan, Rumput, Waktu, Harga


class LapanganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_rumput')


admin.site.register(Lapangan, LapanganAdmin)
admin.site.register(Rumput)
admin.site.register(Waktu)
admin.site.register(Harga)
