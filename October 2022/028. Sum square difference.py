#Link: https://projecteuler.net/problem=6

'''
Question:
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

sum_of_sqaures = 0
square_of_sum = 0

for x in range(1, 101):
    sum_of_sqaures += x**2
    
for y in range(1, 101):
    square_of_sum += y
    
difference =  (square_of_sum**2) - sum_of_sqaures

print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is", difference)

