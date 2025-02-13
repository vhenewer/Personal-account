from amount import Amount

class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        transaction = Amount(amount, 'DEPOSIT')
        self.transactions.append(transaction)
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            transaction = Amount(amount, 'WITHDRAWAL')
            self.transactions.append(transaction)
            self.balance -= amount

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account {self.account_number} - {self.account_holder}, Balance: {self.balance}"

    def __add__(self, amount: float):
        self.deposit(amount)

    def __sub__(self, amount: float):
        self.withdraw(amount)
