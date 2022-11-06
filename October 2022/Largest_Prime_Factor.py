#Question Link: https://projecteuler.net/problem=3

'''
Question:
What is the largest prime factor of the number 600851475143 ?
'''

from math import *

num = 600851475143

max_div = ceil(sqrt(num))

prime_number = 2

for x in range(2, max_div):
    prime = 1

    for y in range(2,x):
        if x % y == 0:
            prime = 0
            break

    if prime == 1:
        if (num % x == 0):
            prime_number = x
    
    if (x % 100000 == 0):
        print(x)

print("Largest prime factor of the number 600851475143: ", prime_number)