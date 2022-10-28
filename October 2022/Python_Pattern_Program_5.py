#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Question:
Print the following python pattern.
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
'''

for rows in range(1, 7):
    #Print space
    for space in range(1, rows+1):
        print(" ", end='')
    
    #Print Star
    for star in range(7,rows,-1):
        print("*", end='')
    print("")


# In[ ]:




