#Question Link: https://projecteuler.net/problem=10
'''
Question:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import time
from math import *

start = time.time()

num = 2
sum = 0

while (num < 2000000):
    prime = True

    for x in range(2, 1 + floor(sqrt(num))):
        if num % x == 0:
            prime = False
            break

    else:
        sum += num

    num += 1

print("Sum of all primes below 2 million = ", sum)

end = time.time()

print("Time taken to execute the code: ", (end-start), "seconds")