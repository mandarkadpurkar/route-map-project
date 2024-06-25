from django.core.management.base import BaseCommand
from geopy.distance import geodesic
import random
from myapp.models import Hub

class Command(BaseCommand):
    help = 'Generate random hubs within a 50 km radius in Pune'

    def handle(self, *args, **kwargs):
        pune_center = (18.5204, 73.8567)
        hubs = []

        while len(hubs) < 5:
            random_point = (
                pune_center[0] + random.uniform(-0.45, 0.45),
                pune_center[1] + random.uniform(-0.45, 0.45)
            )

            if geodesic(pune_center, random_point).km <= 50:
                hubs.append(random_point)

        for lat, lon in hubs:
            hub = Hub(latitude=lat, longitude=lon)
            hub.save()
            self.stdout.write(self.style.SUCCESS(f'Generated hub at: {lat}, {lon}'))
