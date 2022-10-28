#Link: https://projecteuler.net/problem=5
 
'''
Question:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def isDivisibleBy2(number):
    for x in range(2, 21):
        if number%x != 0:
            return False
    return True

number = 2520

while True:
    if isDivisibleBy2(number):
        break
    number += 20

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", number)


# In[ ]:




