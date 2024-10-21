"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt, pow

def special_pythagorean_triplet():
    a = 1
    b = 2
    while b < 500:
        for a in range(1, b):
            if (int(pow(a,2)) + int(pow(b,2))) == int(pow((1000 - a - b), 2)):
                return a, b, 1000 - a - b
            a += 1
        b += 1
        

if __name__ == "__main__":
    print(special_pythagorean_triplet())