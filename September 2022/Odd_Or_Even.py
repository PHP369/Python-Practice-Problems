#Question Link: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

'''
Question:
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. 
'''

num = int(input("Enter any integer: "))
if num % 2 == 0:
    print("The number ",num ,"is an even number.")
else:
    print("The number ",num ,"is an odd number.")
