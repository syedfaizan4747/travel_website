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


    for driver_data in drivers:
        Driver.objects.get_or_create(
            name=driver_data["name"],
            defaults=driver_data,
        )
        Driver = apps.get_model("tours", "Driver")

    drivers = [
        {
            "name": "Syed Nayaz",
            "experience": "20",
            "details": "Experienced and professional driver with good knowledge of local routes.",
        },
        {
            "name": "Mohmmed Arbaz",
            "experience": "13",
            "details": "Experienced and professional driver with good knowledge of local routes.",
        },
        {
            "name": "Syed yaseen",
            "experience": "15",
            "details": "Professional and experienced driver focused on safe, comfortable and reliable travel. Experienced in local and outstation journeys.",
        },
        {
            "name": "Syed Kazim",
            "experience": "15",
            "details": "Professional and experienced driver focused on safe, comfortable and reliable travel. Experienced in local and outstation journeys.",
        },
    ]

   


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