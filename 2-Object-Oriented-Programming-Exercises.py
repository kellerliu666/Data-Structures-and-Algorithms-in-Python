#--------------------------------------------------------------------------------------------------------------
# Write a Python class, Flower, that has three instance variables of type str, int, and float, that 
# respectively represent the name of the flower, its number of petals, and its price. Your class must include 
# a constructor method that initializes each variable to an appropriate value, and your class should include 
# methods for setting the value of each type, and retrieving the value of each type.
class Flower:
    def __init__(self, name, petals, price):
        if isinstance(name, str) and isinstance(petals, int) and isinstance(price, float):
            self.name = name
            self.petals = petals
            self.price = price
        else:
            '''ensure the type of value is correct'''
            raise TypeError('Error')
    '''methods for setting value and retrieving value'''  
    def set_name(self, val):   
        self.name = val
    def get_name(self):        
        print self.name
    def set_petals(self, val):
        self.petals = val
    def get_petals(self):
        print self.petals
    def set_price(self, val):
        self.price = val
    def get_price(self):
        print self.price
'''testing'''    
if __name__ == '__main__':            
    a = Flower('Lily', 6, 12.5)
    b = Flower('Rose', 10, 23.0)
    a.get_name()
    b.get_petals()
    b.set_petals(9)
    b.get_petals()

#--------------------------------------------------------------------------------------------------------------   
# revise the charge and make_payment methods of the CreditCard class to ensure that the caller sends a number
# as a parameter. Raises a ValueError if a negative value is sent to make_payment method.
def charge(self, price):
    if not isinstance(price, (int, float)):
        raise TypeError('Must be number!')
    if price + self.balance > self.limit: 
        return False                     
    else:
        self.balance += price
        return True

def make_payment(self, amount):
    if not isinstance(amount, (int, float)):
        raise TypeError('Must be number!')
    elif amount < 0:
        raise ValueError('Must be positive!')
    self.balance −= amount
    
#--------------------------------------------------------------------------------------------------------------   
#
