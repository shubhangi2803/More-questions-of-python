# 1. Write a Python program to create a lambda function that adds 15 to
# a given number passed in as an argument, also create a lambda function
# that multiplies argument x with argument y and print the result.

p=lambda x:print(x+15)
q=lambda x,y:print(x*y)

x=int(input("Enter a number to add 15 to it : "))
p(x)
y=int(input("Enter one more number to add 15 to it : "))
p(y)
a,b=map(int,input("Enter two numbers to multiply : ").split())
q(a,b)

