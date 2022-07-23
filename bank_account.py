#Bank Account
#In this project, we’ll create a Python class that can be used to create and manipulate a personal bank account.

#The bank account class you’ll create should have methods for each of the following:

#Accepting deposits
#Allowing withdrawals
#Showing the balance
#Showing the details of the account

class BankAccount:
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Account: {n}\nBalance: ${b:.2f}'.format(n=self.name, b=self.balance)

    def show_balance(self):
        print('Account Balance: ${:.2f}'.format(self.balance))

    def deposit(self, amount):
        if amount <= 0:
            print('Error: Invalid Amount')
            return
        else:
            print('${:.2f} is currently being deposited...'.format(amount))
            self.balance += amount
            print('...Deposit Successfull.')
            self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print('Error: Insuffecient Balance.')
            return
        else:
            print("processing withdraw of ${:.2f}".format(amount))
            self.balance -= amount
            print('....Withdraw Sucessfull')
            self.show_balance()


my_account = BankAccount('richi')
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
my_account.withdraw(10000)
my_account.deposit(0)
print(my_account)
