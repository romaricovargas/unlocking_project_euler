'''
The Fibonacci sequence is defined by the recurrence relation:

    F(n) = F(n-1) + F(n-2), where F(1)=1 and F(2) = 1

Hence the first 12 terms will be:

    F(1) = 1
    F(2) = 1
    F(3) = 2
    F(4) = 3
    F(5) = 5
    F(6) = 8
    F(7) = 13
    F(8) = 21
    F(9) = 34
    F(10) = 55
    F(11) = 89
    F(12) = 144
 
The 12th term, F(12), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Note:

Python only allow calling a recursive function for 1000 times.
This can be extended to 10**6 times using the following codes:

    import sys
    sys.setrecursionlimit(10**6)

However, this is still not enough for my solution. 
To address this, I placed the recursive call within a loop, 
ensuring that each recursive call does not exceed 1000 iterations.

'''

#import sys
#sys.setrecursionlimit(10**6)

def problem_0025():

    def fibonacci(x, y, i, max):
        #recursive function that will generate the fibonacci series until max is reached
        j = i + 1
        z = x + y
        if z < max:
            return fibonacci(y, z, j, max)
        else:
            return y, z, j

    # Initial values
    p = 200  #number of digits
    a = 1    #first number
    b = 1    #second number
    c = 2    #index of second number

    for p in range(200, 1001, 200):
        a, b, c = fibonacci(a,b,c,10**(p-1))            # invoke recursive iterations several times
        
    return c     

print(problem_0025())