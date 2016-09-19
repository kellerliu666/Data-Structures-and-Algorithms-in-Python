# Invoke function in traditional way, like:
sorted(data)
# When classes define one or more methods:
data.sort()
# But be aware, sorted(data) only made a copy from data and returned the sorted copy.
data = [2,6,4,3,5,8,7,0,1]
print sorted(data)
print data
# data.sort() changed data itself.
