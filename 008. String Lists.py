#Question Link: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

'''
Question:
Ask the user for a string and print out whether this string is a palindrome
or not.
'''

s = input("Enter any string: ")
S = [*s]

l = len(s)

b = []
c = []

if l%2 == 0:
    S1 = l/2
    S2 = l/2
    b = S[0:int(S1)]
    c = S[int(S2):int(l)]
    d = list(reversed(c))
    if b == d:
        print("The string you entered is a palindrome.")
    else:
        print("The string you entered is not a palindrome.")
else:
    S1 = ((l+1)/2)-1
    S2 = (l+1)/2
    b = S[0:int(S1)]
    c = S[int(S2):l]
    d = list(reversed(c))
    if b == d:
        print("The string you entered is a palindrome.")
    else:
        print("The string you entered is not a palindrome.")
    
