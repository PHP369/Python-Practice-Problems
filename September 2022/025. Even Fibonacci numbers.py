#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Question Link: https://projecteuler.net/problem=2

'''
Question:
By considering the terms in the Fibonacci sequence whose values do not exceed four 
million, find the sum of the even-valued terms.
'''

total = 0

term1 = 1
term2 = 1
term3 = 2

while term3 < 4000000:
    term3 = term1 + term2
    if term3 % 2 == 0:
        total += term3
    term1 = term2
    term2 = term3

print("The sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million is", total)

