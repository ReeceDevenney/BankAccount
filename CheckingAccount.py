from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number)
        self.transfer_limit = transfer_limit
        self.__routing_number = routing_number


    def deposit(self, value):
        self.current_balance = self.current_balance + value

    def withdraw(self, value):
        if value <= self.transfer_limit:
            if self.current_balance - value > self.minimum_balance:
                self.current_balance = self.current_balance - value           
            else:
                print("balance too low, can not withdraw")
        else:
            print("transfer ammount exceeds transfer limit")
