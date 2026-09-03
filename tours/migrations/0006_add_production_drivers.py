from django.db import migrations


def add_production_drivers(apps, schema_editor):
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

    for driver_data in drivers:
        Driver.objects.get_or_create(
            name=driver_data["name"],
            defaults=driver_data,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0005_setup_production_data"),
    ]

    operations = [
        migrations.RunPython(add_production_drivers),
    ]