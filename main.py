import math
from Satellites import *


def check_values(min_coord, max_coord, type):
    try:
        num = float(input(type))
        if(num < max_coord and num > min_coord):
            return num
    except:
        print("Некорректные данные. Попробуйте снова.")
        check_values(min_coord, max_coord, type)


def add_satellite():
    satellite_types = {
        '1': 'Гражданский',
        '2': 'Военный',
        '3': 'Метеорологический',
        '4': 'Навигационный',
        '5': 'Разведывательный',
        '6': 'Экспериментальный',
        '7': 'Научный'
    }

    def set_type():
        print("Выберите тип спутника: ")
        for key, value in satellite_types.items():
            print("{0}: {1}".format(key, value))
        choose = input("Выбор: ")

        if choose not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Неправильный выбор. Попробуйте снова.")
        else:
            return satellite_types[choose]

    satellites[f"Спутник {len(satellites) + 1}"] = Satellites(
        check_values(-90, 90, "Координата ширины: "),
        check_values(-180, 180, "Координата долготы: "),
        input("Страна-владелец: "),
        set_type()
    )


def get_distance():

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

        print("Высота спутника", dist, "км")
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


    while True:
        while True:
            target_lat = int(input('Введите координаты широты в градусах: \n'))
            if target_lat < -90 or target_lat > 90:
                print("Неверные координаты широты. Попробуйте снова")
            else:
                while True:
                    target_lon = int(input('Введите координаты долготы в градусах: \n'))
                    if target_lon < -180 or target_lon > 180:
                        print("Неверные координаты долготы. Попробуйте снова")
                    else:
                        break
                break
            
        nearest_satellite = find_nearest_satellite(target_lat, target_lon, satellites)
        print("Ближайший спутник:", nearest_satellite, "\n")

        break


# Словарь спутников с их координатами (ш. и д.)
satellites = {
    'Спутник 1': Satellites(45.467, 9.186, 'Россия', 'Гражданский'),
    'Спутник 2': Satellites(53.3498, 6.2603, 'Россия', 'Экспериментальный'),
    'Спутник 3': Satellites(37.7749, -55.4194, 'Россия', 'Метеорологический'),
    'Спутник 4': Satellites(51.5074, 0.1278, 'Россия', 'Научный')
}

while True:
    print("Выберите действие:\n"
          "[1] Отобразить спутники и информацию о них\n"
          "[2] Соединиться со спутником\n"
          "[3] Добавить спутник\n"
          )

    menu = input("Выбор: ")

    if menu not in ['1', '2', '3']:
        print("Неправильный выбор. Попробуйте снова.")
    else:
        if menu == '1':
            for key, value in satellites.items():
                print(key, value.print_info())
            print()
        elif menu == '2':
            get_distance()
        elif menu == '3':
            add_satellite()
