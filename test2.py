# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Add two numbers 

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

total = num1 + num2

print("total: ",total)



# Factorial of a number through conditional statements

num = int(input("Enter a non-negative number: "))
factorial = 1
if num < 0:
    print("Sorry, you can't find factorial here for negative numbers")
    
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
    

# Factorial of a number through functions

num = input("Enter a number: ")

def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("Sorry, you can't find factorial here for negative numbers")
    else:
        return n * factorial(n-1)
print(factorial(int(num)))

