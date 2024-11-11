'''
PROBLEM 0006
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is,
    3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
'''

def problem0006(sum_a=0, sum_b=0, i=0):
    i += 1
    sum_a += i**2
    sum_b += i
    if i < 100:
        sum_a, sum_b = problem0006(sum_a, sum_b, i)
    if i == 1:
        return (sum_b**2 - sum_a)
    return sum_a, sum_b

print(problem0006())