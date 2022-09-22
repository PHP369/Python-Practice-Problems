#Question Link: https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/

'''
Question:
Create a function in Python that accepts two parameters.
The first will be a list of numbers. The second parameter will be a
string that can be one of the following values: asc, desc, and none.
If the second parameter is "asc," then the function should return a
list with the numbers in ascending order. If it's "desc," then the
list should be in descending order, and if it's "none," it should return
the original list unaltered.
'''

numList = []
num = int(input("Enter the no. of elements you want to add to the list: "))
for x in range(num):
    element = int(input("Enter the element: "))
    numList.append(element)

string = input("Enter a couple of digits in ascending or descending or none of them order: ")
l = string.split("")

print(l)



