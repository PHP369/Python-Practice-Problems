#Question Link: https://www.codechef.com/problems/AIRLINE

t = int(input())

if (t>=1 and t<=36000):
    for i in range(t):
        a,b,c,d,e = map(int, input().split())

        if (a>=1 and a<=10 and b>=1 and b<=10 and c>=1 and c<=10 and d>=15 and d<=20 and e>=5 and e<=10):
            if ((a+b<=d and c<=e) or (b+c<=d and a<=e) or (a+c<=d and b<=e)):
                print("YES")
            else:
                print("NO")