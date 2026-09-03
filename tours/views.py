from django.shortcuts import render
from .models import Car, Driver


def home(request):
    cars = Car.objects.all()
    drivers = Driver.objects.all()

    return render(request, 'home.html', {
        'cars': cars,
        'drivers': drivers,
    })
