#Question Link: https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/

'''
Question:
Write a function in Python that accepts one numeric parameter.
This parameter will be the measure of an angle in radians.
The function should convert the radians into degrees and then
return that value.
'''

print("Please enter the amount of radian in the most simplified form. Take pi as 3.14. Eg: If you want to write 2pi, write 6.28.")
radian = float(input("Enter radians: "))
print("The given radians in degrees is ",(radian*180)/3.14)
