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

#Ask user how many rows of pattern he/she wants to be printed.
num_of_rows = abs(int(input("Enter the no. of rows of the pattern to be drawn: ")))

#For no. of rows
for rows in range(num_of_rows):
     
     #For no. of spaces
     for space in range(rows):
          print(" ", end='')

     #For no. of columns
     for cols in range(num_of_rows, rows, -1):
          print("*", end=" ")
     
     print()