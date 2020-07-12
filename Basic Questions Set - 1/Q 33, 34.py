# 33. Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero.
# 34. Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.

x,y,z=map(int,input("Enter three numbers : ").split())
if x==y or y==z or z==x:
    print("Two numbers are equal, so, result will be zero ! ")
    print(0)
else:
    print("Sum of three numbers : ")
    print(x+y+z)
