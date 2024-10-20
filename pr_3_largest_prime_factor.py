"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
"""
def prime_number(n: int):
    for i in range(n -1 , 1, -1):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n: int):
    for i in range(n - 1, 1, -1):
        print (i)
        # if n % i == 0:
        #     if prime_number(i):
        #         return i


if __name__ == "__main__":
    print(prime_number(600851475143))
