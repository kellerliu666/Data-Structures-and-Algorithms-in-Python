#--------------------------------------------------------------------------------------------------------------
Chapter 3 Algorithm Analysis
#--------------------------------------------------------------------------------------------------------------
# When we talk about Asymptotic Analysis, here is a running time list of each function(from fast to slow)
1   
log n 
n
n log n   # running time less or equal than n log n is considered efficient
n^2
n^3
...
n^7    # running time more or equal than n^7 is considered slow
2^n
n!
n^n

#--------------------------------------------------------------------------------------------------------------
# Big-Oh is the upper bound of a function. If there is a constant C, makes T(n) <= C*f(n), when n is infinity:
T(n) belongs to O(f(n))
# Big-Omega is the lower bound of a function. If there is a constant C, makes T(n) >= C*g(n), when n is infinity:
T(n) belongs to Omega(g(n))
# Big-Theta is both the upper & lower bound of a function. If there is a constant C, makes 
# C*g(n) >= T(n) >= C*g(n), when n is infinity:
T(n) belongs to Theta(g(n))
# Normally, if T(n) belongs to Theta(f(n)): T(n) belongs to O(f(n)) and T(n) belongs to Omega(f(n)).

#--------------------------------------------------------------------------------------------------------------
# Element Uniqueness problem, when using Sorting as a Problem-Solving Tool
def is_dis(lst):
    lst.sort()
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            return False
    return True
# In the best situation, sort() only have to run O(n), worst situation could run O(n*log n). (Quicksort)
# We can also use set() to solve this better
def is_dis(lst):
    if len(lst) != len(set(lst)):
        return False
    return True
# set() could run O(1) in best case, worst case could be O(n). So faster than sort() in particular situation.

#--------------------------------------------------------------------------------------------------------------
# 

