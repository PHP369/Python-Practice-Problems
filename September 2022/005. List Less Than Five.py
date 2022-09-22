#Question Link: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

'''
Question:
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that
are less than 5.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Enter any integer: "))

b = []

for x in a:
    if x < num:
        b.append(x)

print(b)
