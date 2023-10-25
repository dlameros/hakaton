import math
from Satellites import *

def add_satellite():
    satellites[f"Спутник {len(satellites)+1}"] = Satellites(
            float(input("Координата ширины: ")),
            float(input("Координата долготы: ")),
            input("Страна-владелец: "),
            input("Тип устройства: ")
        )

def get_distance():
    target_lat = int(input('Введите координаты ширины в градусах: '))
    target_lon = int(input('Введите координаты долготы в градусах: '))

    def distance(lat1, lon1, lat2, lon2):
        # Преобразовать градусы в радианы
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        # Рассчитать разницу между широтой и долготой
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Расчет гаверсинуса
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2

        # Расчет центрального угла
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Расчет расстояния на поверхности земли
        r = 6371  # Радиус Земли в километрах
        dist = r * c

        return dist

    def find_nearest_satellite(target_lat, target_lon, satellites):
        min_dist = float('inf')  # Начальное значение минимального расстояния
        nearest_satellite = ''

        for satellite, coords in satellites.items():
            satellite_lat, satellite_lon = coords.return_val()
            dist = distance(target_lat, target_lon, satellite_lat, satellite_lon)

            if dist < min_dist:
                min_dist = dist
                nearest_satellite = satellite

        return nearest_satellite

    # Пример использования

    # Задаем целевую точку на земле

    # Находим ближайший спутник к заданной точке на земле
    nearest_satellite = find_nearest_satellite(target_lat, target_lon, satellites)

    print("Ближайший спутник:", nearest_satellite, "\n")

# Словарь спутников с их координатами (ш. и д.)
satellites = {
    'Спутник 1': Satellites(45.467, 9.186, 'Страна-владелец: Россия', 'Предназначение: Гражданский'),
    'Спутник 2': Satellites(53.3498, -6.2603, 'Страна-владелец: Россия', 'Предназначение: Гражданский'),
    'Спутник 3': Satellites(37.7749, -122.4194, 'Страна-владелец: Россия', 'Предназначение: Гражданский'),
    'Спутник 4': Satellites(51.5074, -0.1278, 'Страна-владелец: Россия', 'Предназначение: Гражданский')
}

while True:
    print("Выберите действие:\n[1] Отобразить спутники и информацию о них\n[2] Соединиться со спутником\n[3] Добавить спутник\n")
    menu = int(input("Выбор: "))

    if menu == 1:
        for key, value in satellites.items():
            print("{0}: {1}".format(key, value.print_info()))
        print()
    elif menu == 2:
        get_distance()
    elif menu == 3:
        add_satellite()
