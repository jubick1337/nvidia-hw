class Value:
    def __init__(self):
        self._val = 0

    def __set__(self, instance, value):
        self._val = value * (1 - instance.commission)

    def __get__(self, instance, owner):
        return self._val


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
