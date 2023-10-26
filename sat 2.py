from geopy.distance import geodesic
def find_optimal_satellite(satellites, area_of_interest):
    satellite_distances = []
    for satellite in satellites:
        distance = geodesic((satellite.current_latitude, satellite.current_longitude), area_of_interest).km
        satellite_distances.append((satellite, distance))
    sorted_satellites = sorted(satellite_distances, key=lambda x: x[1])
    for i in range(len(sorted_satellites)-1):
        radial_difference = geodesic((sorted_satellites[i][0].current_latitude, sorted_satellites[i][0].current_longitude), (sorted_satellites[i+1][0].current_latitude, sorted_satellites[i+1][0].current_longitude)).km
        if radial_difference < threshold:
            selected_satellite = sorted_satellites[i][0]
    if not selected_satellite:
        selected_satellite = sorted_satellites[0][0]
    # расчет необходимого количества витков для перемещения выбранного спутника
    # выполнение дополнительных действий, если это необходимо
    return selected_satellite
