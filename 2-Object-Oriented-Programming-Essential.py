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
# Here is a simple and basic example of creating class, which is CreditCard:
class CreditCard:
    def __init__(self, name, bank, account, limit):
        self.name = name
        self.name = bank
        self.account = account
        self.limit = limit
        self.balance = 0
    def get_customer(self):
        return self.name
    def get_bank(self):
        return self.bank
    def get_account(self):
        return self.account
    def get_balance(self):
        return self.balance
    def get_limit(self):
        return self.limit
    def make_payment(self, amount):
        self.balance -= amount
    def charge(self, price):
        if price + self.balance > self.limit:
            return False
        else: 
            self.balance += price
            return True

#--------------------------------------------------------------------------------------------------------------
#
