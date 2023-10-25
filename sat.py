from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4
from math import degrees
import datetime
from math import radians, cos, sin
line1 = '1 06235U 72082A   23297.48450924 -.00000006  00000-0  25309-3 0  9993'
line2 = '2 06235 102.0042 288.8635 0003770 209.3723 305.2886 12.53169402333857'

satellite = twoline2rv(line1, line2, wgs72)

# Создаем объект даты и времени
year, month, day, hour, minute, second = 2023, 10, 26, 0, 0, 0
date = datetime.datetime(year, month, day, hour, minute, second)

# Вычисляем позицию спутника в заданный момент времени
position, velocity = satellite.propagate(date.year, date.month, date.day, date.hour, date.minute, date.second)

# Координаты точки на Земле
lat, lon = 55.75, 37.62  # Москва

# Меняем углы в радианы
lat = radians(lat)
lon = radians(lon)

# Радиус Земли в километрах
radius = 6371

# Вычисляем расстояние
dx = cos(position[0]) * cos(position[1]) - cos(lat) * cos(lon)
dy = cos(position[0]) * sin(position[1]) - cos(lat) * sin(lon)
dz = sin(position[0]) - sin(lat)
distance = radius * (dx**2 + dy**2 + dz**2)**0.5

print(f"Расстояние от спутника до точки на Земле: {round(distance, 2)} км")