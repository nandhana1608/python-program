#10. Write a Python program to create a BankAccount class with attributes such as account number, 
# account holder name, account type, and balance. Use a constructor to initialize the attributes and implement
# methods to deposit money, withdraw money, and display the account details and current balance. Create one or
# more objects to demonstrate the functionality.

class BankAccount:

    def __init__(self, account_no, name, account_type, balance):
        self.account_no = account_no
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawal successful")

    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)


# User input
account_no = input("Enter account number: ")
name = input("Enter account holder name: ")
account_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Create account
account = BankAccount(account_no, name, account_type, balance)

# Deposit
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

# Withdraw
withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

# Display
account.display()