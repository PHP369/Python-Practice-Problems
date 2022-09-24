#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question Link: https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

'''
Question:
Implement a function that takes as input three variables, and returns 
the largest of the three. Do this without using the Python max() function!
'''

num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))
num3 = float(input("Enter your 3rd number: "))

if num1>num2 and num1>num3:
    print("The first number ",num1 ," is the largest of the three.")
elif num2>num1 and num2>num3:
    print("The second number ",num2 ," is the largest of the three.")
elif num3>num1 and num3>num2:
    print("The third number ",num3 ," is the largest of the three.")

