
Chapter 1 Python Primer

# Be aware, some methods, like <sorted(list)>, only made a sorted copy from data and returned the sorted copy. 
# However, some methods, like <list.sort()>, changed data itself.</p>
>>> a_lst = [2, 6, 4, 3, 5, 8, 7, 0, 1]
>>> print sorted(a_lst)
>>> print a_lst
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[2, 6, 4, 3, 5, 8, 7, 0, 1]
>>> a_lst.sort()
>>> print a_lst
[0, 1, 2, 3, 4, 5, 6, 7, 8]

# Some methods that don't change original data.
>>> import string
>>> a_str = 'aaaabbbbbccc'
>>> table = string.maketrans('c', 'a')
>>> print a_str.translate(table)
>>> print a_str
aaaabbbbbaaa
aaaabbbbbccc
>>> print a_str.replace('c', 'a')
>>> print a_str
aaaabbbbbaaa
aaaabbbbbccc

