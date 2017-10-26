'''
Lab 31: ATM

Let's represent an ATM with a class containing two attributes: a balance and an interest rate.
A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account

Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal,
add a string to a list saying 'user deposited $15' or 'user withdrew $15'.
Add a new function print_transactions() to your class for printing out the list of transactions.


'''


class AtmAccount:
    def __init__(self, balance, interest_rate = 0.1):
        self.balance = balance      # varaibles on right of = need to match what's called in the init function
        self.interest_rate = interest_rate
        self.transaction_history = []           # this needs to be here so that it saves all the data that is added


    def check_balance(self):
        return self.balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.transaction_history.append(f'user deposited ${deposit_amount}')

    def check_withdrawal(self, withdrawal_amount):
        return withdrawal_amount < self.balance

    def withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        self.transaction_history.append(f'user withdrew ${withdrawal_amount}')

    def calc_interest(self):
        return self.balance * self.interest_rate

    def print_transactions(self):
        for line in self.transaction_history:
            print(line)


account1 = AtmAccount(20)

account_management = ''

while account_management != 'done':
    account_management = input(
        '\nWhat would you like to do with your account? Choose: check balance, deposit, make withdrawal, history, or done: ')

    if account_management in 'check balance':
        print(account1.check_balance())

    elif account_management in 'deposit':
        deposit = float(input('\nHow much is the deposit? '))
        account1.deposit(deposit)       # this is function(variable)

    elif account_management in 'history':
        account1.print_transactions()
        print(f"Your current balance is: ${account1.check_balance()}")

    elif account_management in 'make withdrawal':
        withdraw = float(input('\nHow much is the withdrawal? '))
        if account1.check_withdrawal(withdraw):
            account1.withdraw(withdraw)
        else:
            print('\nYou don\'t have enough dollars for that.')


print(f'\nYour current balance is: ${account1.check_balance()}')