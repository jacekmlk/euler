"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

import time
from math import sqrt

def erastotenes_sieve(limit: int) -> list:
    sieve = [True] * limit
    maximum = int(sqrt(limit))
    
    for i, value in enumerate(sieve[: maximum], 2):
        if value == True:
            for x in range(2*i, limit, i):
                sieve[x] = False
    
    primes = -1
    for i, value in enumerate(sieve):
        if value == True:
            primes += i
            
    return primes

if __name__ == "__main__":
    start = time.time()
    print(erastotenes_sieve(2000000))
    stop = time.time()
    print(stop-start)
    