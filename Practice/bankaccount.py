# Practice Session 1
# Prince Oforh Asiedu
# 15-03-22
from logger import Logger 

LOGGER = Logger()
LOGGER.filename = 'error_log.txt'
class BankAccount():
    """A class for conducting bank account operations"""

    def __init__(self, initial_balance=None):
        self._balance = initial_balance # the initial amount in the account
        self._account_history = 'account_log.txt' # a list record of operations performed during account lifetime
        self._action = ''
        
        

    def deposit(self, amount):
        """Add money to the account."""
        if not amount <= 0:
            self._balance += amount # increment account balance by amount
            self.account_logger(action='d', amount=amount)
        else:
            LOGGER.warn('Invalid attempt to deposit amount below zero') 

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if not amount > self._balance:
            self._balance -= amount  # deduct the amount to withdraw from the account
            self.account_logger(action='w', amount=amount)
        else: 
            LOGGER.error('Insufficient funds to proceed with withdrawal')
        

    def get_balance(self):
        """Return account balance."""
        self.account_logger(action='g')
        return self._balance # fetch account balance 
    
    def print_account_statement(self):
        """Print the account statement."""
        self.account_logger(action='p')
        try:
            with open(self._account_history, 'r') as account_log:
                acc_log = account_log.readlines()

            if acc_log:
                acc_log = [line.strip() for line in acc_log if acc_log]
                for line in acc_log:
                    print(line)
            else:
                print('You haven\'t performed any transactions on your account yet!')
            print("\nThanks for banking with us.")
        
        except Exception as error:
            LOGGER.critical('Program has encountered a critical error!')
    
    def account_logger(self, action=None, amount=0):
        """Update account transaction log"""
        statement = 'Your Account History\n----------------------\n' # This will be used as file heading
        # Automatically create the 'account_log.txt' file where we log 
        # account transactions using the with context context manager
        # It eliminates the error of not closing the file before exiting
        # our program which could cause problems later when we try 
        # writing to the file
        with open(self._account_history, 'r+') as account_log: # open the file in read-write mode
            lines = account_log.readlines() 
           
            if not lines:                       # Check to see if file has any contents
                account_log.write(statement)    # if not, append our header to it.

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
        if not other <= 0:
            self._balance += other
            self.account_logger(action='d', amount=other)
        else:
            LOGGER.warn('Invalid attempt to deposit amount below zero')
    
    def __radd__(self, other):
        if not other <= 0:
            self._balance += other
            self.account_logger(action='d', amount=other)
        else:
            LOGGER.warn('Invalid attempt to deposit amount below zero')
    
    def __sub__(self, other):
        if not other > self._balance:
            self._balance -= other
            self.account_logger(action='w', amount=other)
        else:
            LOGGER.error('Insufficient funds to proceed with withdrawal')
    
    def __rsub__(self, other):
        print('Please state your transaction properly')


if __name__ == '__main__':
    a = BankAccount(500)
    a + 250
    a - 15000
    a.print_account_statement()
