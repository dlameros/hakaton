class Satellites:
    def __init__(self, lon, lat, country, type):
        self.lon = lon
        self.lat = lat
        self.country = country
        self.type = type

    def print_info(self):
        return f"Координата ширины: {self.lon}", f"Координата долготы: {self.lat}", f"Страна-владелец: {self.country}", f"Тип устройства: {self.type}"

    def return_val(self):
        return self.lon, self.lat