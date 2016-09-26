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
        
>>> my_account = BankAccount(10)
>>> my_account.withdraw(15)
>>> my_account.deposit(20)
>>> print my_account.get_balance(), my_account.get_fees()
10 5   # balance is $10, total fee is $5 

#--------------------------------------------------------------------------------------------------------------
# Testing is important. Generally, we use 'if' sentence below to start a testing:
if __name__ == '__main__': 
# So that testing content will be executed when Python is invoked directly on this module, but not when the module is 
# imported for use in a larger software project.

#--------------------------------------------------------------------------------------------------------------
# When define a class, there are many Special Methods to indicate Common Syntax, like:
__add__(self, other): self + other
__mul__(self, other): self * other
__getitem__(self, k): self.a[k]
__setitem__(self, k, v): self.a[k] = v
__len__(self): len(self)
# etc...etc...etc...

#--------------------------------------------------------------------------------------------------------------
# Here is an example of some Special Methods:
class Gen:
    '''Create a class named Gen'''
    def __init__(self, d):
        '''Set digits of Gen class'''
        self.coords = [0] * d
    def __len__(self):
        '''Return length of digits of Gen'''
        return len(self.coords)
    def __setitem__(self, i, val):
        '''Set given value to certain position'''
        self.coords[i] = val
    def __getitem__(self, i):
        '''Return given value at certain position'''
        return self.coords[i]
    def __mul__(self, other):
        '''Return multiple of two Gen class'''
        result = Gen(len(self.coords))
        for j in range(len(self.coords)):
            result[j] = self.coords[j] * other.coords[j]
        return result
    def __str__(self):
        '''Present Gen class by certain string'''
        return '<' + str(self.coords)[1:-1] + '>'

if __name__ == '__main__':
    '''Testing'''
    G1 = Gen(2)  # Create <0,0>
    G2 = Gen(2)  # Create <0,0>
    G1[0] = 2    
    G1[1] = 2    # <2,2>
    G2[0] = 3    
    G2[1] = 4    # <3,4>
    Gr = G1 * G2 # <6,8>
    print Gr     # print out <6,8>
    
#--------------------------------------------------------------------------------------------------------------
# Another example by creating iteration class Range (similar to built-in range). In this method, __len__ and
# __getitem__ are essential.
class Range:
    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError('Step cannot be 0')
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step
    def __len__(self):
        return (self.stop - self.start + self.step - 1) // self.step
    def __getitem__(self, k):
        if k < 0:
            k = len(self) - 1 + k     # Convert negative k to be reasonable
        if not 0 <= k < len(self):
            raise IndexError('Out of range')
        return self.start + (k * self.step)

# There is another way to achive this iterator, by using __iter__ and __next__.
class Iterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def next_method(self):
        self.start += 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        else:
            result = self.start
            self.next_method()   
            return result

#--------------------------------------------------------------------------------------------------------------
# Example of the use of inheritance, continue using class Iterator.
class SimpleIter(Iterator):
    def __init__(self, start, stop, step):
        Iterator.__init__(self, start, stop)
        self.step = step
    def next_method(self):
        self.start += self.step
        
class MultiIter(Iterator):
    def __init__(self, start, stop, base):
        Iterator.__init__(self, start, stop)
        self.base = base
    def next_method(self):
        self.start *= self.base
        
# By using iteration and inheritance, we can do a lot intersting sequence, like "Fibonacci".
class Fibonacci(Iterator):
    def __init__(self, start, stop, second):
        Iterator.__init__(self, start, stop)
        self.second = second
    def next_method(self):
        temp = self.start
        self.start = self.second
        self.second = temp + self.second

>>> print [i for i in Fibonacci(0, 10000, 1)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

#--------------------------------------------------------------------------------------------------------------
#
      
      
