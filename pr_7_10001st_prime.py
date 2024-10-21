"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""
from math import sqrt

def prime_number(iter: str) -> int:
    count = 1
    n = 1
    while count < iter:
        n += 2
        if all(n % i != 0 for i in range(2, int(sqrt(n)) + 1)):
            count += 1
    return n


if __name__ == "__main__":
    print(prime_number(10001))