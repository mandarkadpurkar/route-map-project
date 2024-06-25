

from django.http import JsonResponse
from django.shortcuts import render
from geopy.distance import geodesic
from .models import Hub

def find_all_hubs(user_location):
    hubs = Hub.objects.all()
    hubs_data = []

    for hub in hubs:
        hub_location = (hub.latitude, hub.longitude)
        distance = geodesic(user_location, hub_location).km
        hubs_data.append({
            'latitude': hub.latitude,
            'longitude': hub.longitude,
            'distance': distance
        })

    return hubs_data

def get_location(request):
    latitude = float(request.GET.get('lat'))
    longitude = float(request.GET.get('lon'))
    user_location = (latitude, longitude)
    
    hubs_data = find_all_hubs(user_location)
    
    return JsonResponse({'hubs': hubs_data})

def home(request):
    return render(request, 'home.html')
