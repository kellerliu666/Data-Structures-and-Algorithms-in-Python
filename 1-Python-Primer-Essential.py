
Chapter 1 Python Primer

# Be aware, some methods, like <sorted(list)>, only made a sorted copy from data and returned the sorted copy. 
# However, some methods, like <list.sort()>, changed data itself.</p>
>>> a_lst = [2, 6, 4, 3, 5, 8, 7, 0, 1]
>>> print sorted(a_lst)
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> print a_lst
[2, 6, 4, 3, 5, 8, 7, 0, 1]
>>> a_lst.sort()
>>> print a_lst
[0, 1, 2, 3, 4, 5, 6, 7, 8]


# Some methods that don't change original data.
>>> import string                       # Import Module
>>> a_str = 'aaaabbbbbccc'
>>> table = string.maketrans('c', 'a')
>>> print a_str.translate(table)
aaaabbbbbaaa
>>> print a_str
aaaabbbbbccc
>>> print a_str.replace('c', 'a')
aaaabbbbbaaa
>>> print a_str
aaaabbbbbccc


# Set, similar to list, but has no duplicates in it, which means set can be a good way to check if there's any
# repeated data in structure. Set follows Hash, so there is no particular order in set, but good for searching
# an particular element.
>>> a_lst = [1, 2, 3, 3, 4]
>>> print len(a_lst)
5
>>> print len(set(a_lst))     # Convert a list into set, then count it
4                             # Length of list is different from length of set, duplicates is true


# If a return statement in a function is executed, the function immediately ends.


# Yield statement can make a generator, for instance, prime number generator:
def is_prime(n):                         # Judge whether it's a prime number, return True or False
    if n > 1: 
        if n==2: return True
        if n % 2 == 0: return False
        for m in range(2, n):
            if n % m == 0:
                return False
        return True
    return False
    
def prime_generator(l):                  # Prime number generator
    for n in l:
        if is_prime(n): 
            yield n

prime_lmt = int(input())                 # Generate all prime number in particular range
prime_range = range(0, prime_lmt + 1)
prime_list = []
for result in prime_generator(lst):
    prime_list.append(result)
print prime_list
    
>>> 20
[2, 3, 5, 7, 11, 13, 17, 19]

# Conditional Expression syntax can be a simple control structure.
Return True if data == target else False


# Comprehension Syntax could be effective as well.
[n*n for n in list]       # Return a list
(n*n for n in list)       # Return a generator
{n*n for n in list}       # Return a set


# Python can also generate random number or pick up a number randomly from a sequence.
>>> import random                # Import Module
>>> print random.randint(1,10)
6                                # Answer here could be any integer randomly between 1 and 10
>>> a_lst = [3, 5, 7]
>>> print random.choice(a_lst)
5                                # Answer here could be randomly from 3, 5 or 7
>>> random.shuffle(a_lst)
>>> print a
[9, 3, 4]                        # Method here shuffles the given sequence
