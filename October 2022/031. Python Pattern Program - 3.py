'''
Question:
Print the follwing python pattern.
     *    
    * *
   * * * 
  * * * * 
 * * * * *
* * * * * *
'''

for rows in range(1, 7):
    for space in range(6, rows, -1):
        print(" ", end='')
    for cols in range(rows):
        print("*", end=" ")
    print("")
    

