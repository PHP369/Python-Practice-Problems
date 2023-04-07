#Question Link: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

'''
Question:
Write a program (using functions!) that asks the user for a long string containing multiple 
words. Print back to the user the same string, except with the words in backwards order.
'''

string = input("Enter a long string containing multiple words: ")

myList = string.split(" ")

myList.reverse()

rString = " ".join(myList)

print("Reversed string: ", rString)


# In[ ]:




