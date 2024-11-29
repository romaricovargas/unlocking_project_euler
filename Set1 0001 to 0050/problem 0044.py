'''
Problem 44
PENTAGON NUMBERS

Pentagon numbers are generated by the formula P(n) = n(3n-1)/2. 
The first ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145 ...

It can be seen that P(4) + P(1) = 22 + 70 = 92 = P(8). 
However, their difference, 70-22=48, is not pentagonal.
Find the pair of pentagonal numbers, P(j) and P(k) for which 
their sum and difference are pentagonal and D = |P(k) - P(j)| is minimised; 
what is the value of D?

'''

def problem_0044(limit=1000):
    pentagonal = {1:1}   # dictionary of pentagonal numbers with initial first entry.
    n = 2                # current n

    def compute_pentagonal(x):
        return int(x*((3*x)-1)/2)

    while len(pentagonal) < limit:
        pentagonal[n] = compute_pentagonal(n)
        n += 1

    for k, v in pentagonal.items():
        print(k, " : ", v) 


problem_0044(100)