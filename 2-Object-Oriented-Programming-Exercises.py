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
# Implement the mul method for the Vector class of Section 2.3.3, so that the expression u v returns a scalar 
# that represents the dot product of the vectors.
def __mul__(self, other):
        '''returns a scalar that represents 
        the dot product of the vectors'''
        result = Vector(len(self.coords))
        temp = 0
        for j in range(len(self.coords)):
            temp += self.coords[j] * other.coords[j]
            result[j] = temp
        return result

#--------------------------------------------------------------------------------------------------------------   
# In Vector class, if a single integer is sent, it produces a vector of that dimension with all zeros, but if a 
# sequence of numbers is provided, it produces a vector with coordinates based on that sequence.
def __init__(self, d):
    '''modify __init__ function by using <isinstance> to achieve this'''
    if isinstance(d, list):
        self.coords = d
    elif isinstance(d, int):
        self.coords = [0] * d

#--------------------------------------------------------------------------------------------------------------   
# Draw a class inheritance diagram for set of classes.
class Animal(object):
    def __init__(self):
        pass   
class Goat(Animal):
    def __init__(self, _tail):
        Animal.__init__(self)
        self._tail = _tail
    def milk(self):
        pass
    def jump(self):
        pass
class Pig(Animal):
    def __init__(self, _nose):
        Animal.__init__(self)
        self._nose = _nose
    def eat(self, food):
        self.food = food
    def wallow(self):
        pass
class Horse(Animal):
    def __init__(self, _height, _color):
        Animal.__init__(self)
        self._height = _height
        self._color = _color
    def run(self):
        pass
    def jump(self):
        pass       
class Racer(Horse):
    def __init__(self, _height, _color):
        Horse.__init__(self, _height, _color)
    def race(self):
        pass
class Equestrian(Horse):
    def __init__(self, _height, _color, _weight):
        Horse.__init__(self, _height, _color)
        self._weight = _weight
    def trot(self):
        pass
    def is_trained(self):
        pass
    
#--------------------------------------------------------------------------------------------------------------   
# Give a single implementation of Vector. __mul__ that uses run-time type checking to support both syntaxes
# u*v and u*k, where u and v designate vector instances and k represents a number.
def __mul__(self, base, other = None):
    '''Return multiple of two Gen class'''
    result = Gen(len(self.coords))
    if isinstance(base, int):
        for j in range(len(self.coords)):
            result[j] = self.coords[j] * base
    else:
        other = base
        base = None
        for j in range(len(self.coords)):
            result[j] = self.coords[j] * other.coords[j]
    return result

#--------------------------------------------------------------------------------------------------------------   
#
