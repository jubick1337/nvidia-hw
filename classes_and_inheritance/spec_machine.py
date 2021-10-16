from classes_and_inheritance.car_base import CarBase


class SpecMachine(CarBase):
    def __init__(self, brand: str, photo_file_name: str, carrying: str, extra: str):
        super().__init__(brand, photo_file_name, carrying, "spec_machine")
        self.extra = extra
