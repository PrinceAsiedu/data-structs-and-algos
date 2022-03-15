# Practice Session 1
# Prince Oforh Asiedu
# 15-03-22

class BankAccount:
    """A class for conducting bank account operations"""

    def __init__(self, initial_balance=None):
        self._balance = initial_balance # the initial amount in the account
        self._account_history = [] # a list record of operations performed during account lifetime
        self._action = ''
    
    def deposit(self, amount):
        """Add money to the account."""
        self._balance += amount # increment account balance by amount
        self.account_logger(action='d', amount=amount)

    def withdraw(self, amount):
        """Withdraw money from the account."""
        self._balance -= amount  # deduct the amount to withdraw from the account
        self.account_logger(action='w', amount=amount)

    def get_balance(self):
        """Return account balance."""
        self.account_logger(action='g')
        return self._balance # fetch account balance 
    
    def print_account_statement(self):
        """Print the account statement."""
        if self._account_history:
            print("Your Account Statement\n----------------------")
            for action in self._account_history:
                print(str(action))
        else:
            print('You haven\'t performed any transactions on your account yet!')
        print("\nThanks for banking with us.")
        self.account_logger(action='p')
    
    def account_logger(self, action=None, amount=0):
        """Update account transaction log"""
        if action == 'd' and amount > 0:
            self._account_history.append('DEPOSIT: %s' % amount)

        elif action == 'w' and amount > 0:
            self._account_history.append('WITHDRAWAL: %s' % amount)

        elif action == 'g':
            self._account_history.append('BALANCE REQUEST: %s' % self._balance)

        elif action == 'p':
            self._account_history.append('ACCOUNT STATEMENT REQUEST') 

    def __str__(self):
        print('Your balance: ', self._balance())
    
    # Some implied methods for quick and easy operations on account balance
    def __add__(self, other):
        self._balance += other
        self.account_logger(action='d', amount=other)
    
    def __radd__(self, other):
        self._balance += other
        self.account_logger(action='d', amount=other)
    
    def __sub__(self, other):
        self._balance -= other
        self.account_logger(action='w', amount=other)
    
    def __rsub__(self, other):
        print('Please state your transaction properly')


if __name__ == '__main__':
    a = BankAccount(500)
    a.deposit(150)
    a.withdraw(50)
    print(a.get_balance())
    print('\n')
    a + 250
    100-a
    a.print_account_statement()
    print(a.get_balance())
