import csv

from classes_and_inheritance.car import Car
from classes_and_inheritance.spec_machine import SpecMachine
from classes_and_inheritance.truck import Truck


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        next(reader)
        for row in reader:
            car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
            if car_type == "car":
                car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
            elif car_type == "truck":
                car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
            elif car_type == "spec_machine":
                car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
    return car_list
