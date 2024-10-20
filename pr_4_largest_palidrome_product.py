"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 \times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def digit_list(number: int) -> bool:
    digits = []
    while number > 0:
        mod = number % 10
        number = number // 10
        digits.append(mod)
    
    digits.reverse()
    return digits


def check_palidrome(digits: list):
    iter = len(digits) // 2
    for i in range(iter):
        if digits[i] != digits[-i-1]:
            return False
    return True


def brute_largest_palidrome(digits_number: int):
    max = 0
    x = 9
    for i in range(1, digits_number + 1):
        max += x
        x *= 10
    mn = max // 10
    
    for a in range(max, mn, -1):
        for b in range(max, mn, -1):
            number = a * b
            if check_palidrome(digit_list(number)):
                return number, a, b
        
print(brute_largest_palidrome(3))