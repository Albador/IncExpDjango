from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description', 'value', 'currency', 'date', 'user')


# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Booking, BookingAdmin)
