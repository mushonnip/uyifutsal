from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
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


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(Lapangan, LapanganAdmin)
admin.site.register(Rumput)
admin.site.register(Waktu, WaktuAdmin)
admin.site.register(Harga, HargaAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)