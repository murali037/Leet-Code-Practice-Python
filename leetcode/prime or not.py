#%% prime or not

import time

def is_prime_v1(n):
    if n ==1:
        return False
    elif n==2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

t0 = time.time()
for n in range(1,50000):
    print(n, is_prime_v1(n))
t1 = time.time()
print("time required:", t1-t0) 

#%% using square root
import math

def is_prime_v2(n):
    if n ==1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))+1
    for i in range(3,max_divisor,2):
        if n % i == 0:
            #print(n, i, math.floor(math.sqrt(n))+1)
            return False
    return True

t0 = time.time()
for n in range(1,1000000):
    print(n, is_prime_v2(n))
t1 = time.time()
print("time required:", t1-t0)

#%%

for i in range(3,100,2):
    print(i)