'''
Question:
Print the follwing python pattern, dynamically.
     *    
    * *
   * * * 
  * * * * 
 * * * * *
* * * * * *
'''

#Ask user how many rows of pattern he/she wants to be printed.
num_of_rows = abs(int(input("Enter the no. of rows of the pattern to be drawn: ")))

#For no. of rows
for rows in range(1, num_of_rows + 1):

    #For no. of spaces
    for space in range(num_of_rows, rows, -1):
        print(" ", end='')

    #For no. of columns
    for cols in range(rows):
        print("*", end=" ")

    print("")