#Question Link: https://pythonbasics.org/for-loops/

'''
Question:
Create a loop that counts all even numbers to the number that user enters.
'''

limit = int(input("Enter the number upto which you need to find the sum of all even numbers: "))
total = 0

for x in range(0,limit+1,2):
    total += x
    
print("The required sum of even numbers is", total)

