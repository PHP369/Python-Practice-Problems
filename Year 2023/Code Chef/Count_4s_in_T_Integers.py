#Question Link: https://www.codechef.com/problems/LUCKYFR
#Program to count number of '4's in T integers

t = int(input())

intList = []

for x in range(t):
    count=0
    a = int(input())
    b = a
    while(b>0):
        rem = b % 10
        if (rem == 4):
            count += 1
        b = b / 10
    print(count)