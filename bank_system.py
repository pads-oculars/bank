# bank_system.py

from customer_management import CustomerManagement
from account_management import AccountManagement
from transaction_management import TransactionManagement

class BankSystem:
    def __init__(self):
        self.customer_manager = CustomerManagement()
        self.account_manager = AccountManagement()
        self.transaction_manager = TransactionManagement()

    def start(self):
        # Your banking system logic goes here
        pass
