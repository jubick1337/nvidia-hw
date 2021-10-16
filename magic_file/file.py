import tempfile
import uuid

from pathlib import Path


class File:
    def __init__(self, path: str):
        self.path = Path(path)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            self.data = self.path.open("r").read()
        else:
            self.data = ""

    def read(self) -> str:
        return self.data

    def write(self, data: str) -> int:
        self.data = data
        self.path.open("w").write(self.data)
        return len(self.data)

    def __add__(self, other):
        new_file = File(Path(tempfile.gettempdir()) / str(uuid.uuid4()))
        new_file.write(self.data + other.data)
        return new_file

    def __str__(self):
        return str(self.path)

    def __iter__(self):
        return iter(self.data.split("\n"))
