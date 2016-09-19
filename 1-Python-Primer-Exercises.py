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
