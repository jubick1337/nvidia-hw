from abc import ABC
from pathlib import Path
from typing import List


class CarBase(ABC):
    _allowed_photo_ext = [".jpg", ".jpeg", ".png", ".gif"]

    def __init__(self, brand: str, photo_file_name: str, carrying: str, car_type: str = None):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = Path(photo_file_name)
        if self.get_photo_file_ext() not in self._get_allowed_photo_ext():
            raise AttributeError(
                f"File ext {self.get_photo_file_ext()} is not one of allowed extensions: {self._get_allowed_photo_ext()}"
            )
        self.carrying = carrying

    def get_photo_file_ext(self) -> str:
        return self.photo_file_name.suffix

    @classmethod
    def _get_allowed_photo_ext(cls) -> List[str]:
        return cls._allowed_photo_ext
