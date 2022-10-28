#Question Link: https://projecteuler.net/problem=3

'''
Question:
What is the largest prime factor of the number 600851475143 ?
'''

num = 600851475143
prime_number = 0

for x in range(1,num):
    if num % x == 0:
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            prime_number = x

print(prime_number)

