"""
pseudocode:
for i in range(2, sqrt(num)):
    if num % i == 0:
       return False
return True
"""
from math import sqrt


def prime_num(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


is_prime = prime_num(25)

if is_prime:
    print("Prime number")
else:
    print("Not Prime number")
