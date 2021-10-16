from classes_and_inheritance.car_base import CarBase


class Car(CarBase):
    def __init__(self, brand: str, photo_file_name: str, carrying: str, passenger_seats_count: str):
        super().__init__(brand, photo_file_name, carrying, "car")
        self.passenger_seats_count = passenger_seats_count
