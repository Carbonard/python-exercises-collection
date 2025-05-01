# Fibonacci Number Calculator (3 Methods)

# This script calculates the n-th Fibonacci number using three different approaches:
#
# 1. Recursive (`fibonacci_number_recursive`):
#    - Uses direct recursion based on the Fibonacci definition.
#    - Simple but inefficient for large n due to repeated calculations.
#
# 2. Iterative (`fibonacci_number_loop`):
#    - Uses a for-loop to build up the Fibonacci sequence.
#    - Much more efficient than recursion and suitable for large n.
#
# 3. Functional (`fibonacci_number_reduce`):
#    - Uses `functools.reduce` to compute Fibonacci numbers in a functional style.
#    - Efficient and concise, though less readable to beginners.
#
# The script calculates the 15 first Fibonacci numbers using all three methods, and creates a graphic comparing the different calculation times.

print("importing")
from time import time
print("importing")
from numbers_manipulation import scientific_notation
print("importing")
import seaborn as sns
print("importing")
import matplotlib.pyplot as plt
print("importing")

def fibonacci_number_recursive(n):
    if n==1 or n==2: return 1
    else: return fibonacci_number_recursive(n-2)+fibonacci_number_recursive(n-1)

def fibonacci_number_loop(n):
    if n==1 or n==2: return 1
    else:
        a=1
        b=1
        for i in range(3,n+1):
            a,b=b,a+b
        return b

from functools import reduce
def fibonacci_number_reduce(n):
    if n==1 or n==2: return 1
    else:
        return reduce(lambda s,i: (s[1],s[0]+s[1]), range(3,n+1),(1,1))[1]

# A class to store method information and timing data for Fibonacci calculation methods.
class method:
    def __init__(self, name, funct, color='black'):
        self.name = name
        self.funct = funct
        self.times = [0] # List to store times taken for calculate each Fibonacci number.
        # The list is initialized with 0 at index 0 to align times[n] with the calculation time for the n-th Fibonacci number.
        self.color = color # Used in the graphic.
    def add_time(self,t):
        self.times.append(t)

# Agrouping the different methods.
methods = [
    method("recursion",fibonacci_number_recursive, 'red'),
    method("loop",fibonacci_number_loop, 'blue'),
    method("reduce",fibonacci_number_reduce, 'green')
]

# To calculate Fibonacci numbers while registering calculation times.
def calculate_time(method, n):
    start = time()
    fibonacci_number = method.funct(n)
    end = time()
    method.add_time(end-start)
    return fibonacci_number

# Using the previous function with the different methods to calculate first Fibonacci numbers.
for n in range(1,15):
    for method in methods:
        fibonacci_number = calculate_time(method,n)
        # Print the results for small numbers (uncomment if desired).
        # print(f"The {n}th Fibbonachi number is {fibonacci_number} and it took {scientific_notation(method.times[len(method.times)-1],2)} seconds with {method.name} method.")

# Plot the comparision of calculation times.
for method in methods:
    sns.lineplot(x=list(range(len(method.times))),y=method.times, color=method.color)
plt.show()
