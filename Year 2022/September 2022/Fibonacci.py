#Question Link: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

'''
Question:
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
'''

num = abs(int(input("How many Fibonnaci numbers you want to generate?: ")))

Fibonnaci = [1, 1]

num1 = 1
num2 = 1

for x in range(num-2):
    num3 = num1 + num2
    Fibonnaci.append(num3)
    num1 = num2
    num2 = num3

print(Fibonnaci)