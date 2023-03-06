#Link: https://projecteuler.net/problem=7

'''
Question:
What is the 10001st prime number?
'''

import time

start = time.time()

num = 2
prime_count = 0
prime_num = 0


while (prime_count < 10001):
    prime = True

    for x in range(2, num):
        if num % x == 0:
            prime = False
            break

    else:
        prime_count += 1
        prime_num = num

    num += 1

print("10001st Prime Number = ", prime_num)

end = time.time()

print("Time taken to execute the code: ", (end-start), "seconds")