from classes_and_inheritance.utils import get_car_list


def test_simple():
    cars = get_car_list("../data.csv")
    assert cars[0].passenger_seats_count == "4"
    assert cars[1].get_body_volume() == 60.0
    assert cars[2].get_body_volume() == 0.0
