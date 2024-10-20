"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible divisible with no remainder by all of the numbers from 1 to 20?
"""
def smallest_multiple(max_div: int):
    dividers = list(range(max_div, (max_div // 2), -1))
    number = 20
    
    div_num = 0
    while div_num < len(dividers):
        if number % dividers[div_num] != 0:
            number += dividers[0]
            div_num = 0
        else:
            div_num += 1

    return number


if __name__ == "__main__":
    print(smallest_multiple(20))