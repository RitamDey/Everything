from functools import total_ordering


@total_ordering  # Used as a shortcut when __eq__ and __lt__ defined
class Account:
    """ A simple account class """

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __init__(self, owner, amount=0):

        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __str__(self):
        """
        The “informal” or nicely printable string representation
        of an object. This is for the enduser.
        """
        return 'Account of {} with starting amount {}'.format(
                                            self.owner, self.amount)

    def __repr__(self):
        """
        The “official” string representation of an object.
        This is how you would make an object of the class.
        The goal of __repr__ is to be unambiguous.
        """
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self._transactions[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        """
        This is the normal `+` functionality.
        `__radd__` is used when we want reversed add functionality
        """
        owner = f"{self.owner}&{other.owner}"
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

    def __call__(self):
        """
        One can made a python class callable by using
        `__call__` method.
        """
        print(f"Balance for", self.owner)
        print(f'Start amount: {self.amount}')
        print("Transactions:")
        for tran in self:
            print(tran)
        print(f"Balance: {self.balance}")

    """
    A context manager is a simple “protocol” (or interface) that your
    object needs to follow so it can be used with the with statement.
    Basically all you need to do is add __enter__ and __exit__ methods to
    an object if you want it to function as a context manager.
    """
    def __enter__(self):
        print("ENTER WITH: Making backup of transactions for rollback")
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            self._transactions = self._copy_transactions
            print("Rolling back")
            print('Transaction resulted in {} ({})'.format(
                                                exc_type.__name__,
                                                exc_val
                                                ))
        else:
            print('Transaction OK')


def validate_transaction(acc, amount_to_add):
    with acc as a:
        print('Adding {} to amount'.format(amount_to_add))
        a.add_transaction(amount_to_add)
        print('New balance {}'.format(a.balance))

        if a.balance < 0:
            raise ValueError('can\'t go to debt')


if __name__ == '__main__':
    acc = Account('bob', 10)
    print(str(acc))
    print(acc)
    print(repr(acc))

    acc.add_transaction(20)
    acc.add_transaction(-10)
    acc.add_transaction(50)
    acc.add_transaction(-20)
    acc.add_transaction(30)

    print(acc.balance)

    print(len(acc))
    print(reversed(acc))

    acc2 = Account('tim', 100)
    acc2.add_transaction(20)
    acc2.add_transaction(40)
    print(acc2.balance)

    print(acc2 > acc)
    print(acc2 < acc)
    print(acc2 == acc)

    acc3 = acc + acc2
    print(acc3.amount)
    print(acc3.balance)

    acc()
    acc2()
    acc3()

    acc4 = Account('sue', 10)
    print('Balance start: {}'.format(acc4.balance))
    validate_transaction(acc4, 20)
    print('Balance end: {}'.format(acc4.balance))

    try:
        validate_transaction(acc4, -50)
    except ValueError as exc:
        print(exc)

    print('Balance end {}'.format(acc4.balance))

