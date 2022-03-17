# Practice Session 1
# Prince Oforh Asiedu
# 15-03-22

class BankAccount:
    """A class for conducting bank account operations"""

    def __init__(self, initial_balance=None):
        self._balance = initial_balance # the initial amount in the account
        self._account_history = 'account_log.txt' # a list record of operations performed during account lifetime
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
        with open(self._account_history, 'r') as account_log:
            acc_log = account_log.readlines()

        if acc_log:
            acc_log = [line.strip() for line in acc_log if acc_log]
            for action in acc_log:
                print(str(action))
        else:
            print('You haven\'t performed any transactions on your account yet!')
        print("\nThanks for banking with us.")
        self.account_logger(action='p')
    
    def account_logger(self, action=None, amount=0):
        """Update account transaction log"""
        statement = 'Your Account History\n----------------------\n'
        with open(self._account_history, 'r+') as account_log:
            lines = account_log.readlines()
            if not lines:
                account_log.write(statement)

            if action == 'd' and amount > 0:
                account_log.write('DEPOSIT: %s\n' % amount)

            elif action == 'w' and amount > 0:
                account_log.write('WITHDRAWAL: %s\n' % amount)

            elif action == 'g':
                account_log.write('BALANCE REQUEST: %s\n' % self._balance)

            elif action == 'p':
                account_log.write('ACCOUNT STATEMENT REQUEST\n')

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
    
    a + 250
    a.print_account_statement()
