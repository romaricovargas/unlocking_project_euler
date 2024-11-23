'''
PROBLEM 0031

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?
'''

def problem_0031():

    def distribute(d, c, m, i, u, g, s, t):

        if i < len(c)-1:
            t = distribute(d, c.copy(), m, i+1, u, g, s, t)

        if u >= d[i] and c[i] < m[i]:
            c[i] = c[i] + 1
            s = s + d[i]
            u = u - d[i]
            if s == g:
                t = t + 1
            t = distribute(d, c, m, i, u, g, s, t)

        return t
   
    d = [200, 100, 50, 20, 10, 5, 2, 1]     # denomination
    c = [0, 0, 0, 0, 0, 0, 0, 0]            # count in every denomination
    m = [1, 2, 4, 10, 20, 40, 100, 200]     # max count in every denomination
    i = 0                                   # index of current denomination
    u = 200                                 # undistributed money
    g = 200                                 # goal amount
    s = 0                                   # sum of money
    t = 0                                   # number of combinations

    return distribute(d, c, m, i, u, g, s, t)

print(problem_0031())

