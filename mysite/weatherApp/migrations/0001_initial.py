# Generated by Django 5.0.3 on 2024-03-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeatherInfo",
            fields=[
                ("metStationId", models.IntegerField()),
                ("dataCollectionType", models.CharField(max_length=50)),
                ("dateTaken", models.DateTimeField(primary_key=True, serialize=False)),
                ("windSpeed", models.DecimalField(decimal_places=3, max_digits=10)),
                ("windDirection", models.DecimalField(decimal_places=3, max_digits=10)),
                ("temperature", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "solarRadiation",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("humidity", models.DecimalField(decimal_places=3, max_digits=10)),
                ("uComponent", models.DecimalField(decimal_places=3, max_digits=10)),
                ("vComponent", models.DecimalField(decimal_places=3, max_digits=10)),
                ("sigmaTheta", models.DecimalField(decimal_places=3, max_digits=10)),
                ("hStability", models.IntegerField()),
                ("vStability", models.IntegerField()),
                ("rainfall", models.IntegerField()),
                (
                    "scalarWindSpeed",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                (
                    "scalarWindDirection",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("sigmaWindSpeed", models.IntegerField()),
                ("pressure", models.DecimalField(decimal_places=3, max_digits=10)),
                ("wComponent", models.IntegerField()),
                ("sigmaPhi", models.IntegerField()),
                ("maxWindSpeed", models.DecimalField(decimal_places=3, max_digits=10)),
                ("feelsLike", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "corridorHalfAngle",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("solarRadiationCalculated", models.IntegerField()),
                ("windDirectionText", models.IntegerField()),
                ("rainRate", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "rainRateEstimated",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
            ],
        ),
    ]
