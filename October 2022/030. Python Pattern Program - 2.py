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
    for cols in range(7,rows,-1):
        print("*", end=' ')
    print("")

