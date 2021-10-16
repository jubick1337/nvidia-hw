from classes_and_inheritance.car_base import CarBase


class Truck(CarBase):
    def __init__(self, brand: str, photo_file_name: str, carrying: str, body_lwh: str):
        super().__init__(brand, photo_file_name, carrying, "truck")
        l_w_h = body_lwh.split("x")
        if len(l_w_h) == 3:
            l_w_h = [float(attr) for attr in l_w_h]
            self.body_length, self.body_width, self.body_height = l_w_h
        else:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height
