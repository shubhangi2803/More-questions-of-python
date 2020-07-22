# 147. Write a Python function to check whether a number is divisible by another number.
#      Accept two integers values form the user.
# 148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
#      Note: Do not use built-in functions.

print("To check if one number is divisible by another number")
x=int(input("Enter number to be checked : "))
y=int(input("Give the other number : "))
if x%y==0:
    print("{} is divisible by {}".format(x,y))
else:
    print("Not divisible")
