class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        print(f"You have deposited ${amount}, your bank account is now ${self.balance + amount}")

    def withdraw(self, amount):
        print(f"You have withdrawed ${amount}, your bank account is now ${self.balance - amount} ")

    def display_info():
        print(f"Your current bank account is now ${self.balance}")


bank1 = BankAccount("John", "1000")
bank2 = BankAccount("Bob", "2500")

bank1.display_info()
bank2.withdraw("500")
bank2.display_info()