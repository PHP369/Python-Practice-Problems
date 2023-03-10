#Question Link: https://www.codechef.com/problems/LUCKYFR
#Program to count number of '4's in T integers

#Reading no. of integers
t = int(input())

for x in range(t):
    count=0
    
    #Reading each integer
    a = int(input())

    #For each integer, counting no. of 4s
    while(a>0):
        rem = a % 10
        if (rem == 4):
            count += 1
        a = a / 10
    
    #Displaying the no. of 4s in each integer
    print(count)