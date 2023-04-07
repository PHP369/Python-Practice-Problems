#Question Link: https://www.codechef.com/problems/NETFLIX

t = int(input())

if (t>=1 and t<=1000):
    for i in range(t):
        a, b, c, x = map(int, input().split())

        if (a>=1 and a<=100 and b>=1 and b<=100 and c>=1 and c<=100 and x>=1 and x<=100):
            if ((a+b>=x) or (b+c>=x) or (a+c>=x)):
                print("YES")
            else:
                print("NO")