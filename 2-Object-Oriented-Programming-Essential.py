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
        self._name = name
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0        
    def get_customer(self):
        return self._name        
    def get_bank(self):
        return self._bank        
    def get_account(self):
        return self._account       
    def get_balance(self):
        return self._balance       
    def get_limit(self):
        return self._limit    
    def make_payment(self, amount):
        self._balance -= amount        
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else: 
            self._balance += price
            return True

#--------------------------------------------------------------------------------------------------------------
#
