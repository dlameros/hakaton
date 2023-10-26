import math
import os
from Satellites import *
from sat import *


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

    satellite_countries = {
        '1': 'Россия',
        '2': 'США',
        '3': 'Италия',
        '4': 'Франция',
        '5': 'Индия',
        '6': 'Республика Беларусь',
        '7': 'Китай'
    }

    def set_type():
        print("Выберите тип спутника:")
        for key, value in satellite_types.items():
            print("{0}: {1}".format(key, value))
        choose = input("Выбор: ")
        if choose not in satellite_types.keys():
            print("Неправильный выбор. Попробуйте снова.")
            return set_type()
        else:
            return satellite_types[choose]

    def set_country():
        print("Выберите страну-владельца спутника: ")
        for key, value in satellite_countries.items():
            print("{0}: {1}".format(key, value))
        choose = input("Выбор: ")
        if choose not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Неправильный выбор. Попробуйте снова.")
            return set_country()
        else:
            return satellite_countries[choose]

    satellite_name = input('\nИмя спутника: ')

    satellites[satellite_name] = Satellites(
        check_values(-90, 90, "Координата ширины: "),
        check_values(-180, 180, "Координата долготы: "),
        set_country(),
        set_type()
    )

    print(f"\nСпутник {list(satellites.keys())[-1]} успешно добавлен")


def get_distance(target_lat, target_lon):
        selected_satellite = exit_distance(target_lat, target_lon)
        return selected_satellite


# Словарь спутников с их координатами (ш. и д.)
satellites = {
    'Спутник 1': Satellites(45.467, 9.186, 'Россия', 'Гражданский'),
    'Спутник 2': Satellites(53.3498, 6.2603, 'Россия', 'Экспериментальный'),
    'Спутник 3': Satellites(37.7749, -55.4194, 'Россия', 'Метеорологический'),
    'Спутник 4': Satellites(51.5074, 0.1278, 'Россия', 'Научный')
}
def task():
    while True:
        print("---------------------------\n"
            "Выберите действие:\n"
            "[1] Отобразить спутники и информацию о них\n"
            "[2] Соединиться со спутником\n"
            "[3] Добавить спутник"
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
                a = get_distance(target_lat, target_lon)
                return (str(a[0]), str(a[2]))
            elif menu == '3':
                add_satellite()