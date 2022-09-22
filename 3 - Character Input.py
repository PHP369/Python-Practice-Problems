#Question Link: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

'''
Question:
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))

from datetime import date
current_year = int(date.today().year)

if age>0 and age<100:
    years_left = 100 - age
    year = current_year + years_left - 1
    print("Hey ", name,", you will turn 100 years old in ",year)
else:
    print("You have already turned 100 years old.")


    

