from django.db import models
from cloudinary.models import CloudinaryField


class Tour(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', folder='tours')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField(max_length=100)
    seats = models.CharField(max_length=50)
    details = models.TextField()
    image = CloudinaryField('image', folder='cars')

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    details = models.TextField()


    def __str__(self):
        return self.name