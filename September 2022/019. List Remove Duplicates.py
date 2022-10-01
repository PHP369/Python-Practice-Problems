#Question Link: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

'''
Question:
Write a program (function!) that takes a list and returns a new list that contains all the 
elements of the first list minus all the duplicates.
'''

list_with_duplicates = []

nums_to_add = int(input("How many numbers you would like to add to the list?: "))
n = abs(nums_to_add)

for x in range(n):
    num = int(input("Enter the number to be added to the list: "))
    list_with_duplicates.append(num)

list_without_duplicates = []

#count = 1

for element in list_with_duplicates:
    if element not in list_without_duplicates:
        list_without_duplicates.append(element)
        
print("")
print("The required list without duplicates is", list_without_duplicates)        


# In[ ]:




