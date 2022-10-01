#Question Link: https://thecleverprogrammer.com/2022/03/31/mean-median-and-mode-using-python/

'''
Question:
Calculate mean, median, and mode using Python.
'''

data_list = []

ask = abs(int(input("How many elements of data you would like to add into the list?: ")))

for x in range(ask):
    element = int(input("Enter any interger to add to the list: "))
    data_list.append(element)
    
#For Mean
mean = sum(data_list)/ask
print("")
print("The mean of the given data is", mean)


# In[ ]:





# In[ ]:




