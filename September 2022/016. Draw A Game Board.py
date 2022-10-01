#Question Link: https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

'''
Question:
Time for some fake graphics! Let’s say we want to draw game boards that look like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Ask the user what size game board they 
want to draw, and draw it for them to the screen using Python’s print statement.
'''

size = abs(int(input("Enter the size (A x A) of the game board you want to be shown: ")))

def row():
    for rows in range(size):
        print(" ---", end='')
    print("")

def col():
    for cols in range(size+1):
        print("|   ", end='')
    print("")
    
for x in range(1,size+1):
    row()
    col()
    if x==size:
        row()
        

        


# In[ ]:




