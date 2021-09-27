from to_json.to_json import to_json

"""
задачу не понял => тесты нормально не писал
"""


@to_json
def get_data():
    return {"data": 42}


@to_json
def get_data_two():
    return {"data1": 32, "data3": 2}


def test_get_data():
    assert get_data == '{"data": 42}'


def test_get_data_two():
    assert get_data_two == '{"data1": 32, "data3": 2}'
