#Question Link: https://projecteuler.net/problem=4
'''
Question:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

largest_palindrome_product = 0
productList = []

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        product = num1 * num2

        if (product > largest_palindrome_product):
            product_str = str(product)
            length = len(product_str)

            str_productList = list(product_str)

            revList = []

            for i in range(length-1, -1, -1):
                revList.append(str_productList[i])

            revProduct = ''.join(revList)

            if (product_str == revProduct):
                largest_palindrome_product = product
            

print(largest_palindrome_product)