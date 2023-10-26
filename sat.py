from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
from math import radians, cos, sin, degrees
import datetime
from geopy.point import Point
from geopy.distance import EARTH_RADIUS, geodesic
import math
import time

satellites = []
with open("satoline.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        line1 = lines[i+1].strip()
        line2 = lines[i+2].strip()
        satellite = twoline2rv(line1, line2, wgs72)
        satellites.append((lines[i], satellite))


# Функция для вычисления расстояния между двумя точками на Земле
def calculate_distance(lat1, lon1, lat2, lon2):
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Расчет гаверсинуса
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2

    # Расчет центрального угла
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    r = 6371
    dist = r * c
    return dist

def radial_dif(lat1, lon1, lat2, lon2):
    # Радиус Земли в километрах
    R = 6371

    # Вычисление разницы в координатах
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Вычисление синусов и косинусов разности широты и разности долготы
    sin_delta_lat = math.sin(delta_lat / 2)
    sin_delta_lon = math.sin(delta_lon / 2)
    cos_lat1 = math.cos(lat1)
    cos_lat2 = math.cos(lat2)

    # Вычисление квадрата радиального различия
    a = sin_delta_lat ** 2 + cos_lat1 * cos_lat2 * sin_delta_lon ** 2

    # Вычисление радиального различия
    radial_difference = 2 * R * math.asin(math.sqrt(a))

    return radial_difference

def exit_distance(target_lat, target_lon):
    satellite_distances = []
    while True:
        for name, satellite in satellites:

            sat_lat, sat_lon = sat_lat_lon(satellite)
            distance = calculate_distance(sat_lat, sat_lon, target_lat, target_lon)
            satellite_distances.append((distance, satellite, name))
        satell = min(satellite_distances)
        return satell
        sorted_satellites = sorted(satellite_distances, key=lambda x: x[1])
        min_radial_difference = float('inf') 
        selected_satellite = None

        for i in range(len(sorted_satellites)-1):
            satellite, _, _ = sorted_satellites[i]
            satellite2, _, _ = sorted_satellites[i+1]
            sat_lat, sat_lon = sat_lat_lon(satellite)
            sat_lat2, sat_lon2 = sat_lat_lon(satellite2)
            radial_difference = radial_dif(sat_lat, sat_lon, sat_lat2, sat_lon2)
            if radial_difference < min_radial_difference:
                min_radial_difference = radial_difference
                selected_satellite = sorted_satellites[i]
        print()
        return selected_satellite
    
def sat_lat_lon(satellite):
    date = datetime.datetime.now()
    position, _ = satellite.propagate(date.year, date.month, date.day, date.hour, date.minute, date.second)
    x, y, z = position[0], position[1], position[2]
    sat_lat = Point(latitude=y/EARTH_RADIUS, longitude=x/EARTH_RADIUS, altitude=z/EARTH_RADIUS).latitude
    sat_lon = Point(latitude=y/EARTH_RADIUS, longitude=x/EARTH_RADIUS, altitude=z/EARTH_RADIUS).longitude
    return (sat_lat, sat_lon)
print(exit_distance(1,6))