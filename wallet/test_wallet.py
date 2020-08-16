import pytest

from .wallet import Wallet, InsufficientAmount


@pytest.mark.skip
@pytest.mark.smoke
def test_default_balance():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_balance():
    wallet = Wallet(100)
    assert wallet.balance == 100


@pytest.mark.smoke
def test_spending():
    wallet = Wallet(100)
    wallet.spend_cash(50)

    assert wallet.balance == 50


@pytest.mark.xfail
def test_spending_fail():
    wallet = Wallet(100)
    wallet.spend_cash(50)

    assert wallet.balance == 40


def test_add_cash():
    wallet = Wallet(20)
    wallet.add_cash(10)

    assert wallet.balance == 30


@pytest.mark.smoke
def test_insufficient_balance():
    wallet = Wallet()

    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(20)


@pytest.mark.skip
@pytest.mark.parametrize('earned,spent,expected', [
    (30, 10, 20),
    (85, 64, 21),
])
def test_transaction(earned, spent, expected):
    wallet = Wallet()
    wallet.add_cash(earned)
    wallet.spend_cash(spent)
    assert wallet.balance == expected
