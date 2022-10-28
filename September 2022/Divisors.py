#Question Link: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

'''
Question: Create a program that asks the user for a number and then prints
out a list of all the divisors of that number.
''' 

num = int(input("Enter any number: "))

myList = []

if num>0:
    for x in range(1, num+1):
        if num%x==0:
            myList.append(x)
    print(myList)
else:
    for x in range(num, 0):
        if num%x==0:
            myList.append(x)
    print(myList)
