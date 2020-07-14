# Write a Python program to add two objects if both objects are an integer type.

def int_sum(x,y):
     if isinstance(x,int) and isinstance(y,int):
          return (x+y)
     raise TypeError('Input must be Integer')

x = input()
y = input()
print(int_sum(x,y))
