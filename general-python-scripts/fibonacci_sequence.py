def fibonacci_number_recurrency(n):
    if n==1 or n==2: return 1
    else: return fibonacci_number_recurrency(n-2)+fibonacci_number_recurrency(n-1)

def fibonacci_number_for(n):
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

for k in range(1,100):
    print(fibonacci_number_for(k))
    print(fibonacci_number_reduce(k))
    print(fibonacci_number_recurrency(k))
