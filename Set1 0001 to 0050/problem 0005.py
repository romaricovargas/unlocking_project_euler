'''
PROBLEM 0005
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def problem0005(n, r=10000000000):             # r is the maximum number of iteration, when reached the program will stop and return 0 
    
    for x in range(n, n*(r+1), n):             # Iterate through the multiples of the number until maximum rounds is reached
        found = False
        for d in range(n-1, round(n/2), -1):   # Check if divisible to all the whole numbers from  round(n/2) to n-1
            if x % d > 0:
                break
            else:
                if d == round(n/2)+1:
                    found = True               # Tag found if divisible to all whole numbers from  round(n/2) to n-1
        if found:
            return x
    return 0
      
print(problem0005(20))