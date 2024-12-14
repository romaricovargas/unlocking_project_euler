'''
PROBLEM 0007

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

'''

from prime_check import is_prime

def problem0006(target, limit=1000000):

    counter = 0
    for x in range(1, limit+1):
        if is_prime(x):
            counter += 1
        if counter == target:
            return x
    return 0          
    

print(problem0006(10001))

