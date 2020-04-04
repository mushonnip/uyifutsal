from django.contrib import admin

from .models import Lapangan, Rumput


class LapanganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_rumput')


admin.site.register(Lapangan, LapanganAdmin)
admin.site.register(Rumput)
