"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
"""
from math import sqrt

def prime_number(n: int):
    for i in range(int(sqrt(n)) - 1, 1, -1):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n: int):
    for i in range(int(sqrt(n)) - 1, 1, -1):
        if n % i == 0:
            if prime_number(i):
                return i


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
