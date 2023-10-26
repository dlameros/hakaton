from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
from math import radians, cos, sin, degrees
import datetime
from geopy.point import Point
from geopy.distance import EARTH_RADIUS
import math
import time

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

def exit_distance(satellites, target_lat, target_lon):
    while True:
        exit_dist = []
        for name, satellite in satellites:
            date = datetime.datetime.now()
            position, _ = satellite.propagate(date.year, date.month, date.day, date.hour, date.minute, date.second)

            x, y, z = position[0], position[1], position[2]
            sat_lat = Point(latitude=y/EARTH_RADIUS, longitude=x/EARTH_RADIUS, altitude=z/EARTH_RADIUS).latitude
            sat_lon = Point(latitude=y/EARTH_RADIUS, longitude=x/EARTH_RADIUS, altitude=z/EARTH_RADIUS).longitude
            distance = calculate_distance(sat_lat, sat_lon, target_lat, target_lon)
            exit_dist.append((distance, name))
        exit_dist = min(exit_dist)
        return exit_dist
def satelite():
    satellites = []
    with open("satoline.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            line1 = lines[i+1].strip()
            line2 = lines[i+2].strip()
            satellite = twoline2rv(line1, line2, wgs72)
            satellites.append((lines[i], satellite))
    return satellites


