# Invoke function in traditional way, like:
sorted(data)

# When classes define one or more methods:
data.sort()

# But be aware, some methods, like <sorted(data)>, only made a sorted copy from data and returned the sorted copy. 
# However, some methods, like <data.sort()>, changed data itself.
>>> data = [2, 6, 4, 3, 5, 8, 7, 0, 1]
>>> print sorted(data)
>>> print data
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[2, 6, 4, 3, 5, 8, 7, 0, 1]
>>> data.sort()
>>> print data
[0, 1, 2, 3, 4, 5, 6, 7, 8]
