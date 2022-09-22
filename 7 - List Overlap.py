#Question Link: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

'''
Question:
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.
'''

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = []
b = []

n = int(input("How many elements do you want to add to your list: "))

for d in range(n):
    e1 = int(input("Enter the element for the first list: "))
    a.append(e1)

for e in range(n+1):
    e2 = int(input("Enter the element for the second list: "))
    b.append(e2)

c = []

for x in a:
    for y in b:
        if x==y and x not in c:
            c.append(x)

c.sort()

print(c)
