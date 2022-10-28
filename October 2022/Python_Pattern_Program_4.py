'''
Question:
Print the following python pattern.
    *
   **
  ***
 ****
*****
'''

for rows in range(1, 6):
    for space in range(1, (6-rows)+1):
        print(" ", end="")
    for cols in range(1, rows+1):
        print("*", end="")
    print("")        

