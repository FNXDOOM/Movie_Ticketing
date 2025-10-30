
# Register your models here.
from django.contrib import admin
from .models import Movie, Show, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_date', 'rating']
    search_fields = ['title', 'genre']
    list_filter = ['genre', 'release_date']

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['movie', 'show_time', 'available_seats', 'price', 'screen']
    list_filter = ['movie', 'show_time']
    search_fields = ['movie__title']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'show', 'seats_booked', 'booking_date', 'total_price']
    list_filter = ['booking_date']
    search_fields = ['user__username', 'show__movie__title']