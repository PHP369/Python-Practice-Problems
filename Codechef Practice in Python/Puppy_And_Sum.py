#Question Link: https://www.codechef.com/problems/PPSUM

t = int(input())

if (t>=1 and t<=16):
    for i in range(t):
        d, n = map(int, input().split())

        if (d>=1 and d<=4 and n>=1 and n<=4):
            for j in range(d):
                sum = (n*(n+1))/2
                n=sum
            print(int(n))