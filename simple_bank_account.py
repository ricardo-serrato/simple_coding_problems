"""
 For this challenge, create a bank account class that has two attributes:

   * owner
   * balance
 and two methods:

   * deposit
   * withdraw
 As an added requirement, withdrawals may not exceed the available balance.

 Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner:  {self.owner}\nAccount Balance:  ${self.balance}"

    def deposit(self, cash_in):
        self.balance += cash_in
        print("Deposited Amount")

    def withdraw(self,cash_out):
        if self.balance - cash_out < 0:
            print("Funds Unavailable!")
        else:
            self.balance -= cash_out
            print("Withdrawal Accepted")


acct1 = Account('Jose',100)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
print(acct1.balance)

acct1.withdraw(75)
print(acct1.balance)

acct1.withdraw(75)
print(acct1.balance)

acct1.withdraw(1)
acct1.withdraw(500)
