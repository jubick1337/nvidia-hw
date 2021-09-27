import os
import subprocess

from typing import List, Optional

import pytest

from kv_store.storage import STORAGE_PATH


def _execute_command(key: str, value=None, capture_output=True) -> Optional[str]:
    command = ["python", "../storage.py", "--key", key]
    if value:
        command.extend(["--val", value])
    res = subprocess.run(
        command,
        capture_output=capture_output,
    )

    if not capture_output:
        return

    return res.stdout.strip().decode()


@pytest.fixture(autouse=True, scope="function")
def flush_storage():
    if STORAGE_PATH.exists():
        os.remove(STORAGE_PATH)
    yield


@pytest.mark.parametrize(
    "key,value,expected",
    [
        ("kek", "lol", "lol"),
        ("key_name", "value", "value"),
        ("kek", "a", "a"),
        ("a", "b", "b"),
        ("1", "a", "a"),
        ("a", "2", "2"),
        (
            "very-long-long-long-long-long-long-long-long-long-long-long"
            "-long-long-long-long-long-long-long-long-long-long-string",
            "2",
            "2",
        ),
    ],
)
def test_single_adding(key: str, value: str, expected: str):
    _execute_command(key, value, False)
    result = _execute_command(key, capture_output=True)
    assert result == expected


@pytest.mark.parametrize(
    "key,value,expected",
    [
        ("kek", ["lol1", "ll2", "ll"], ["lol1", "ll2", "ll"]),
        ("lel", ["a", "b", "c"], ["a", "b", "c"]),
        (
            "multi_key",
            ["value1", "value2"],
            ["value1", "value2"],
        ),
    ],
)
def test_multiple_adding(key: str, value: List[str], expected: List[str]):
    for val in value:
        _execute_command(key, val)
    result = _execute_command(key, capture_output=True)
    assert result == ", ".join(expected).strip()
