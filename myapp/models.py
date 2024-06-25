from django.db import models

class Hub(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Hub({self.latitude}, {self.longitude})"
