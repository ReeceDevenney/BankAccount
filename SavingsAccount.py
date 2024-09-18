from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number)
        self.interest = interest
        self.__routing_number = routing_number

    def earn_interest(self):
        self.current_balance = self.current_balance * (1.0 + self.interest)
        
