'''
Prime number rules:

Rule 0: Not prime if 0 or 1.
Rule 1: Not prime if number ends in 0, 2, 4, 6, 8, and higher than 2.
Rule 2: Not prime if sum of all digits is divisible by 3, except if the given number is 3.
Rule 3: Not prime if number is greater than 5, and last digit is 5.
Rule 4: Not prime if the given number is divisible by any prime number lower than or equal 
        the square root of the given number, except 2, 3, and 5

example: first six prime numbers: 2, 3, 5, 7, 11, and 13

'''

import math

def is_prime(num):
        
    num_text = str(num)

    if num < 2:                                     # Rule 0
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
        
    sqrt_num = math.floor(math.sqrt(num)) + 1
    for b in range(6, sqrt_num):
        if is_prime(b) == True:
            if num % b == 0:                        # Rule 4
                return False

    return True 