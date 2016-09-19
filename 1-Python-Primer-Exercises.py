#--------------------------------------------------------------------------------------------------------------
# Demonstrate how to use Python’s list comprehension syntax to produce [1, 2, 4, 8, 16, 32, 64, 128, 256].
print [2**a for a in range(0, 9)]

#--------------------------------------------------------------------------------------------------------------
# Demonstrate how to use Python’s list comprehension syntax to produce [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
even_lst = [2*a for a in range (0, 10)]
result = []
c = 0
for b in even_lst:
    c += b
    result.append(c)
print result

#--------------------------------------------------------------------------------------------------------------
# Given the string "Let s try, Mike.", this function would return "Lets try Mike".
s = "Let's try, Mike."
import string
for p in string.punctuation:
    s = s.replace(p, " ")
print s

#--------------------------------------------------------------------------------------------------------------
# Write a Python program that can “make change.” Try to design your program so that it returns as few bills and 
# coins as possible.
change = float(input(Enter amount of change: ))
lst = [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.25, 0.1, 0.05, 0.01]
for money in lst:
    count = 0
    if money > change: continue
    while True:
        if money > change:
            break
        if money <= change: 
            count += 1
            change -= money
    print '$', money, 'x', count    # Something wrong with it, try enter 0.03 or 21.22. Feel free correct it

#--------------------------------------------------------------------------------------------------------------
# Design a program that can test Birthday Paradox by a series of experiments on randomly generated birthdays.
import random

def check(birthlst):
    counts = dict()
    for item in birthlst:
        counts[item] = counts.get(item, 0) + 1
        if counts[item] > 1:
            return True
    return False

loop = 10000                                        # I did 10000 experiments here
total = float(loop)
yes = 0
while True:
    if loop == 0: break
    birthlst = list()
    n = 23
    while True:
        if n == 0: break
        date = random.randint(1, 365)
        birthlst.append(date)
        n -= 1
    if check(birthlst): yes += 1
    loop -= 1
prob = yes / total
print prob

#--------------------------------------------------------------------------------------------------------------
