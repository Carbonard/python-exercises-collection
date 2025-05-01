# Fibonacci Number Calculator (3 Methods)

# This script calculates the nth Fibonacci number using three different approaches:
#
# 1. Recursive (`fibonacci_number_recurrency`):
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
# The script prints the Fibonacci numbers from 1 to 99 using all three methods.

from time import time
from numbers_manipulation import scientific_notation

def fibonacci_number_recurrency(n):
    if n==1 or n==2: return 1
    else: return fibonacci_number_recurrency(n-2)+fibonacci_number_recurrency(n-1)

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

methods = {
    "recurrency": fibonacci_number_recurrency,
    "loop": fibonacci_number_loop,
    "reduce": fibonacci_number_reduce
}

def calculate(method, num):
    start = time()
    fib_num = method(num)
    end = time()
    return fib_num, end-start

for k in range(1,50):
    for method, funct in methods.items():
        fib_num, t = calculate(funct,k)
        print(f"The {k}th Fibbonachi number is {fib_num} and it took {scientific_notation(t,2)} seconds with {method} method.")
