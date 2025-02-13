import unittest
from personal_account import PersonalAccount
from amount import Amount


class TestAmount(unittest.TestCase):
    def test_amount_creation(self):
        amount = Amount(100.0, 'DEPOSIT')
        self.assertEqual(amount.amount, 100.0)
        self.assertEqual(amount.transaction_type, 'DEPOSIT')
        self.assertIsNotNone(amount.timestamp)

    def test_amount_str(self):
        amount = Amount(50.0, 'WITHDRAWAL')
        self.assertIn('WITHDRAWAL', str(amount))
        self.assertIn('50.0', str(amount))


class TestPersonalAccount(unittest.TestCase):
    def setUp(self):
        self.account = PersonalAccount(123456, "Venera")

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 0.0)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0].transaction_type, 'DEPOSIT')

    def test_withdraw(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 300)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1].transaction_type, 'WITHDRAWAL')

    def test_withdraw_insufficient_funds(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0.0)
        self.assertEqual(len(self.account.transactions), 0)

    def test_transaction_history(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.deposit(200)
        self.assertEqual(len(self.account.transactions), 3)

    def test_account_number_methods(self):
        self.assertEqual(self.account.get_account_number(), 123456)
        self.account.set_account_number(654321)
        self.assertEqual(self.account.get_account_number(), 654321)

    def test_account_holder_methods(self):
        self.assertEqual(self.account.get_account_holder(), "Venera")
        self.account.set_account_holder("Alex")
        self.assertEqual(self.account.get_account_holder(), "Alex")

    def test_str_method(self):
        self.assertIn("Account", str(self.account))
        self.assertIn("Venera", str(self.account))

    def test_add_operator(self):
        self.account + 100
        self.assertEqual(self.account.get_balance(), 100)

    def test_sub_operator(self):
        self.account + 200
        self.account - 50
        self.assertEqual(self.account.get_balance(), 150)


if __name__ == '__main__':
    unittest.main()
