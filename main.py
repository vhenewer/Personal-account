from personal_account import PersonalAccount
from amount import Amount

account = PersonalAccount(123456, "Venera")

account.deposit(500)

account.withdraw(200)

print(f"Current Balance: {account.get_balance()}")

account.print_transaction_history()

account + 300  # Deposit 300
account - 100  # Withdraw 100

print(account)





