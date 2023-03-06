#Question Link: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

'''
Question:
Ask the user for a string and print out whether this string is a palindrome
or not.
'''

string = input("Enter any string: ")

forward = str(string)
reverse = forward[::-1]

if forward == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")