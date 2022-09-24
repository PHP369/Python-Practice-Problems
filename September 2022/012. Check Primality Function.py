#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question Link: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

'''
Question:
Ask the user for a number and determine whether the number is prime or not.
'''

num = int(input("Enter any number: "))

def main():
    for x in range(2,num):
        if num % x == 0:
            print(num," is not a prime number.")
            break
    else:
        print(num," is a prime number.")

main()           

