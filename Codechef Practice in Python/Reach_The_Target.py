#Question Link: https://www.codechef.com/problems/REACHTARGET

t = int(input())

if (t>=1 and t<=10):
    for i in range(t):
        x, y = map(int, input().split())

        if (x>y and x<=200 and y>=50 and y<x):
            print(x-y)