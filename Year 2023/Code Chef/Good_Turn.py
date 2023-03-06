#Rolling Dices

t = int(input())
if (t>=1 and t<=100):
    for i in range(t):
        X, Y = map(int, input().split())
        if (X>=1 and X<=6 and Y>=1 and Y<=6):
            if (X+Y > 6):
                print("Yes")
            else:
                print("No")