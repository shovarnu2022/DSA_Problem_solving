from math import sqrt


def sieve_prime(num):
    prim_arr = [1]*(num+1)
    prim_arr[0] = 0
    prim_arr[1] = 0
    for i in range(2, int(sqrt(num))+1):
        if prim_arr[i] == 1:
            j = 2
            while i*j < num+1:
                prim_arr[j*i] = 0
                j = j + 1
    return prim_arr


print(sieve_prime(15))
