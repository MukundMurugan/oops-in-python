class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Creating an object of class BankAccount
account = BankAccount(1000)

# Accessing methods to deposit, withdraw, and get balance
account.deposit(500)
account.withdraw(200)
print("Current balance:", account.get_balance())  # Output: Current balance: 1300
