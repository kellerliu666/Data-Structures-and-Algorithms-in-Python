#--------------------------------------------------------------------------------------------------------------
Chapter 2 Object-Oriented Programming
#--------------------------------------------------------------------------------------------------------------
# Form some good coding style in Python.
# Use 4 apaces to indent instead of using Tab.
#--------------------------------------------------------------------------------------------------------------
# Capitalized single noun would be the best choice for Class name.
class Employee or CreditCard:
  
# Usually choose verb in lowercase as Function name.
def make_payment():
  
#--------------------------------------------------------------------------------------------------------------  
# Here is a simple and basic example of creating class, which is BankAccount:
class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """
    fee_count = 0
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance
        """Creates an account with the given balance."""

    def deposit(self, amount):
        self.initial_balance += amount
        """Deposits the amount into the account."""

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal resulting 
        in a negative balance also deducts a penalty fee of 5 dollars
        from the balance.
        """
        self.initial_balance -= amount
        if self.initial_balance < 0:
            self.initial_balance -= 5
            self.fee_count += 1
            
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
        
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee_count*5
        
my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()

#--------------------------------------------------------------------------------------------------------------
#
