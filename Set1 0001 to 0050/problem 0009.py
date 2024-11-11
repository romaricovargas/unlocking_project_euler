'''
PROBLEM 009

A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
   a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def problem0009(n):
    
    max_a = math.ceil(n/3)                        # maximum possible value for 1/3 of n

    for a in range(1, max_a):                     # iterate a from 1 to maximum value
        for b in range(a + 1, n - max_a + 1):     # iterate b from a+1 to the remaining numbers in n
            if b <= a:                            # break if b is not higher than a
                break
            c = n - a - b                         # calculate c
            if c <= b:                            # break if c is not higher than b
                break
            if a**2 + b**2 == c**2:               # check if pythagorean triplets
                #print(" a = ", a)
                #print(" b = ", b)
                #print(" c = ", c)
                #print("a2 + b2 = ", a**2 + b**2 )
                #print("c2      = ", c**2 )
                return (a*b*c)
    return 0        
     
print(problem0009(1000))