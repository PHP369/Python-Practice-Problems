#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question Link: https://thecleverprogrammer.com/2022/03/31/mean-median-and-mode-using-python/

'''
Question:
Calculate Median using Python.
'''

data_list = []

ask = abs(int(input("How many elements of data you would like to add into the list?: ")))

for x in range(ask):
    element = int(input("Enter any interger to add to the list: "))
    data_list.append(element)

#For Median
data_list.sort()

if len(data_list) % 2 == 0:
    m1 = data_list[ask//2]
    m2 = data_list[(ask//2)-1]
    print("The median of the given data is", (m1+m2)/2)
else:
    median = data_list[(ask//2)]
    print("The median of the given data is", median)

