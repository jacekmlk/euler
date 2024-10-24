"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with $1$ and $2$, the first $10$ terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
from time import perf_counter


def sum_even_valued_fibonacci_numbers(limit: int) -> int:
    def fibonacci_numbers(limit: int) -> int:
        numbers = [1, 2]
        
        while numbers[-1] < limit:
            numbers.append(numbers[-2] + numbers[-1])

        return numbers[:-1]
    numbers = fibonacci_numbers(limit)
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i

    return sum


def sum_even_valued_fibonacci_numbers_generator(limit: int) -> int:
    def fibonacci_numbers_generator():
        prev_i = 0
        i = 1
        
        while True:
            yield i
            temp = i
            i = i + prev_i
            prev_i = temp
    
    sum = 0
    for i in fibonacci_numbers_generator():
        if i >= limit:
            break
        elif i % 2 == 0:
            sum += i
            
    return sum


if __name__ == "__main__":
    start_time = perf_counter()
    print(sum_even_valued_fibonacci_numbers_generator(4000000))  
    stop_time = perf_counter()
    print("%.6f" % (stop_time - start_time))
    
    start_time = perf_counter()
    print(sum_even_valued_fibonacci_numbers(4000000))  
    stop_time = perf_counter()
    print("%.6f" % (stop_time - start_time))


