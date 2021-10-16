import pytest

from descriptor.account import Account


@pytest.mark.parametrize(
    "commission,value,expected", [(0.1, 100, 90), (0.2, 100, 80), (0.5, 200, 100), (0.25, 1000, 750)]
)
def test_simple(commission, value, expected):
    account = Account(commission)
    account.amount = value
    assert account.amount == expected
