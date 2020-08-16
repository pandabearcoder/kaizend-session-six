class InsufficientAmount(Exception):
    pass


class Wallet:
    balance = 0

    def __init__(self, balance=0):
        self.balance = balance

    def spend_cash(self, amount):
        if amount > self.balance:
            raise InsufficientAmount('Not available balance to spend {}'.format(self.balance))

        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
