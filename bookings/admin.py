from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Field, Floor, Time, Price, Booking, Profile, Review, Schedule
from django.contrib.auth.models import User

class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor_type')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('price_name', 'price', 'point_required')

class TimeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'price')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_code', 'status', 'user', 'date', 'time')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

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

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'rating')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Floor)
admin.site.register(Time, TimeAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Schedule)
# admin.site.register(User)

