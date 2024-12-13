'''
PROBLEM 0007

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

~~~~~~~~~~~~~~~~~~~~~~~

Prime number rules:

Rule 0: Not prime if 0 or 1.
Rule 1: Not prime if number ends in 0, 2, 4, 6, 8, and higher than 2.
Rule 2: Not prime if sum of all digits is divisible by 3, except if the given number is 3.
Rule 3: Not prime if number is greater than 5, and last digit is 5.
Rule 4: Not prime if the given number is divisible by any prime number lower than or equal 
        the square root of the given number, except 2, 3, and 5

'''

import math

def problem0006(target, limit=1000000):

    def prime_check(num):
        
        num_text = str(num)

        if num == 0 or num == 1:                        # Rule 0
            return False

        if num > 2 and int(num_text[-1]) % 2 == 0:      # Rule 1
            return False
        
        add_digits = 0
        for a in range(0, len(num_text)):
            add_digits += int(num_text[a])
        if add_digits % 3 == 0 and num != 3:            # Rule 2
            return False
        
        if num > 5 and num_text[-1] == "5":             # Rule 3
            return False
        
        sqrt_num = math.ceil(math.sqrt(num))
        check_list = []
        for b in range(6, sqrt_num):
            if prime_check(b) == True:
                check_list.append(b)
        for c in check_list:
            if num % c == 0:                            # Rule 4
                return False

        return True     

    counter = 0
    for x in range(1, limit+1):
        if prime_check(x):
            counter += 1
        if counter == target:
            return x
    return 0
            
    

print(problem0006(10001))
