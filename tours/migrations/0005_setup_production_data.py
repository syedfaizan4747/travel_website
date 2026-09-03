import os
from django.db import migrations
from django.contrib.auth.hashers import make_password


def setup_production_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Car = apps.get_model("tours", "Car")

    # Create live admin account
    username = os.environ.get("ADMIN_USERNAME")
    password = os.environ.get("ADMIN_PASSWORD")

    if username and password:
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if created:
            user.password = make_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()

    # Add the four cars
    cars = [
        {
            "name": "Toyota Innova",
            "seats": "7 Seater",
            "details": "Comfortable Toyota Innova for family and group travel.",
            "image": "cars/innova",
        },
        {
            "name": "Innova Crysta",
            "seats": "7 Seater",
            "details": "Premium Innova Crysta for comfortable long-distance travel.",
            "image": "cars/crysta",
        },
        {
            "name": "Swift Dzire",
            "seats": "4 Seater",
            "details": "Comfortable and economical car for city and local travel.",
            "image": "cars/dzire",
        },
        {
            "name": "Toyota Etios",
            "seats": "4 Seater",
            "details": "Reliable and comfortable Toyota Etios for travel.",
            "image": "cars/toyota",
        },
    ]

    for car_data in cars:
        Car.objects.get_or_create(
            name=car_data["name"],
            defaults=car_data,
        )


def reverse_setup_production_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0004_alter_car_image_alter_tour_image"),
    ]

    operations = [
        migrations.RunPython(
            setup_production_data,
            reverse_setup_production_data,
        ),
    ]