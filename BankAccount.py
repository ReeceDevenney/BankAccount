class BankAccount:
    title = "bank of america"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        
    def deposit(self, value):
        self.current_balance = self.current_balance + value

    def withdraw(self, value):
        if self.current_balance - value > self.minimum_balance:
            self.current_balance = self.current_balance - value           
        else:
            print("balance too low, can not withdraw")

    def print_customer_information(self):
        print("Bank Title: " + BankAccount.title)
        print("Customer Name: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("Minimum Balance: " + str(self.minimum_balance))


