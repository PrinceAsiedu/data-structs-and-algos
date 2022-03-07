# JustPlaying {|:-)
# Prince Asiedu

class BankAccount():

    def __init__(self, person, bank, bal=0):
        self._person = person
        self._bank = bank
        self._balance = bal
    
    def get_acct_bal(self):
        return self._balance
    
    def __add__(self, debit):
        self._balance += debit
    
    def __mul__(self, multiplier):
        self._balance *= multiplier

my_acct = BankAccount('Prince', 'Access Bank', 25)

# my_acct + 3
my_acct * 50

print(my_acct.get_acct_bal())