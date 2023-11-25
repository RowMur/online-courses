def car_fueling(distance, tank_range, stops: list):
    if stops[0] > tank_range:
        return -1

    car_location = 0
    tank_level = tank_range
    stops_count = 0

    for index, stop in enumerate(stops):
        tank_level -= stop - car_location
        car_location = stop

        next_stop = 0
        if index == len(stops) - 1:
            next_stop = distance
        else:
            next_stop = stops[index + 1]

        if next_stop - car_location > tank_range:
            return -1

        if next_stop - car_location > tank_level:
            tank_level = tank_range
            stops_count += 1
    
    return stops_count
        


if __name__ == "__main__":
    total_distance = int(input())
    full_tank_range = int(input())
    n_of_stops = int(input())
    stops = list(map(int, input().split()))

    print(car_fueling(total_distance, full_tank_range, stops))