#Question Link: https://projecteuler.net/problem=9
'''
Question:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time

start = time.time()

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b

        if ((a < b) and (a < c) and (b < c)):
            LHS = (a**2) + (b**2)
            RHS = (c**2)

            if (LHS == RHS):
                sum = a + b + c

                if (sum == 1000):
                    print("Product abc = ", a * b * c)
                    break

end = time.time()

print("Time taken to execute the code: ", (end-start), "seconds")