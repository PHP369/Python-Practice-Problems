#Question Link: https://www.codechef.com/problems/NEARESTEXIT
#Program to determine the nearest exit by the passenger

t = int(input())

if (t>=1 and t<=100):
    
    for x in range(t):
        x = int(input())
        if (x>=1 and x<=100):
            if (x > 50):
                print("RIGHT")
            else:
                print("LEFT")