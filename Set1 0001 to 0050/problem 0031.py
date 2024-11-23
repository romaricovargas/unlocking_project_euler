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
        # d = denomination
        # c = count in every denomination
        # m = max count in every denomination
        # i = index of current denomination
        # u = undistributed money
        # g = goal amount
        # s = sum of money
        # t = number of combinations
            
        print("denominations = ", d, " | counts = ", c,  " | maximum counts = ", m)
        print("undistributed money = ", u, " | current denomination = ", d[i])
        print('----------------------------------------')

        if s == g:
            t = t + 1
            print(' t = ', t)
        
        else:          

            if u >= d[i] and c[i] < m[i]:
                c[i] = c[i] + 1
                s = s + d[i]
                u = u - d[i]
                distribute(d, c, m, i, u, g, s, t)

             



   
    d = [200, 100]   # denomination
    c = [0, 0]       # count in every denomination
    m = [1, 2]       # max count in every denomination
    i = 0            # index of current denomination
    u = 200          # undistributed money
    g = 200          # goal amount
    s = 0            # sum of money
    t = 0            # number of combinations

    distribute(d, c, m, i, u, g, s, t)

problem_0031()

