#Question Link: https://www.codechef.com/problems/GDTURN#:~:text=They%20consider%20a%20turn%20to,whether%20the%20turn%20was%20good
#Program to find whether the turn was good

t = int(input())
if (t>=1 and t<=100):
    for i in range(t):
        X, Y = map(int, input().split())
        if (X>=1 and X<=6 and Y>=1 and Y<=6):
            if (X+Y > 6):
                print("Yes")
            else:
                print("No")