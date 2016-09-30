#--------------------------------------------------------------------------------------------------------------
Chapter 3 Algorithm Analysis
#--------------------------------------------------------------------------------------------------------------
# Running time list(from fast to slow)
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
# 
