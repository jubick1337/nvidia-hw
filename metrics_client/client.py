import socket
import time

from collections import defaultdict
from typing import Optional, Union


class ClientError(Exception):
    pass


class Client:
    def __init__(self, server_ip: str, port: int, timeout: Optional[int] = None):
        self._socket = socket.socket()
        self._socket.connect((server_ip, port))
        self._socket.settimeout(timeout)

    def put(self, metric_name: str, value: Union[int, float], timestamp: Optional[int]):
        if timestamp is None:
            timestamp = int(time.time())
        self._socket.send(f"put {metric_name} {value} {int(timestamp)}\n".encode())
        response = self._read_all()
        if response[:2] != "ok":
            raise ClientError()

    def get(self, metric_name: str):
        self._socket.send(f"get {metric_name}".encode())
        response = self._read_all()
        if response[:2] != "ok":
            raise ClientError()

        result = defaultdict(list)

        for i, line in enumerate(response.split("\n")):
            if not i or line == "":
                continue
            try:
                metric, value, timestamp = line.split()
                result[metric].append((int(timestamp), float(value)))
            except ValueError:
                raise ClientError()

        for key in result.keys():
            result[key] = sorted(result[key], key=lambda x: -x[-1])

        return result

    def _read_all(self):
        raw_response = bytearray()
        chunk = self._socket.recv(1024)
        raw_response.extend(chunk)
        while chunk.decode()[-2:] != "\n\n":
            chunk = self._socket.recv(1024)
            raw_response.extend(chunk)
        return raw_response.decode()
