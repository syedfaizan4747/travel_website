from django.contrib import admin
from .models import Tour, Car, Driver


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'destination',
        'duration',
        'price',
        'featured',
    )

    list_filter = (
        'destination',
        'featured',
    )

    search_fields = (
        'title',
        'destination',
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'seats',
    )

    search_fields = (
        'name',
        'details',
    )


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'experience',
    )

    search_fields = (
        'name',
        'experience',
        'details',
    )