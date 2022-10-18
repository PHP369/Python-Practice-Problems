'''
Question:
Print the following python pattern.
*
* *
* * *
* * * *
* * * * *
* * * * * *
'''

for rows in range(1, 7):
    for cols in range(rows):
        print("*", end=' ')
    print("")

