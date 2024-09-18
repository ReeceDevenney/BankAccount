from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

s1 = SavingsAccount("Reece", 1000, 0, .05, 100, 12345)
s1.deposit(250)
s1.earn_interest()
s1.print_customer_information()

s2 = SavingsAccount("Matt", 300, 0, .1, 101, 12335)
s2.earn_interest()
s2.deposit(100)
s2.print_customer_information()

c1 = CheckingAccount("John", 1400, 350, 421, 83018, 1000)
c1.deposit(950)
c1.withdraw(1000)
c1.print_customer_information()

c2 = CheckingAccount("Ryan", 1000, 900, 123, 54321, 200)
c2.withdraw(500)
c2.withdraw(10)
c2.print_customer_information()


