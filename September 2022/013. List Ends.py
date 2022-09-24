#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question Link: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

'''
Question:
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list.
'''

a = []

nums_to_add = int(input("How many numbers you would like to add to the list?: "))
n = abs(nums_to_add)

for x in range(n):
    num = int(input("Enter the number to be added to the list: "))
    a.append(num)

b = []

count = 1

for y in a:
    if count == 1 or count == n:
        b.append(y)
    count += 1 
        
print("The list of the first and last element from the list of numbers entered: ",b)    


# In[ ]:




