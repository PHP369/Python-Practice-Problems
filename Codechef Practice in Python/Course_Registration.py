#Question Link: https://www.codechef.com/problems/COURSEREG

t = int(input())

if (t>=1 and t<=1000):
	for i in range(t):
		n, m, k = map(int, input().split())
		if (n>=1 and n<=100 and m>=1 and m<=100 and k>=0 and k<=m):
			if (n<=m-k):
				print("YES")
			else:
				print("NO")