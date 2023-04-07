#Question Link: https://www.codechef.com/problems/TAXSAVING

t = int(input())

if (t>=1 and t<=100):
    for i in range(t):
        x , y = map(int, input().split())

        if (x>=1 and y>=1 and x<=100 and y<=100):
            print(x-y)