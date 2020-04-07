# we can calculate the factorial by importing factorial() function from math module.
from math import factorial
print(factorial(9)) 

# or we can calculate factorial manually by using recursive function.
# function recursion means calling a function in its own defination.
# recursive function is very popular because we can solve any problem faster by using it.
def factorial_n(n):
    if n==1:
        return 1
    else:
        return n*factorial_n(n-1)
print(factorial_n(5))