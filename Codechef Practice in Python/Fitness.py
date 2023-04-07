#Question Link: https://www.codechef.com/problems/FIT

t = int(input())

if (t>=1 and t<=10):
    for i in range(t):
        x = int(input())
        if (x>=1 and x<=10):
            print(2*x*5)