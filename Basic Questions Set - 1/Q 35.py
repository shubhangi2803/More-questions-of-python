# 35. Write a Python program that will return true if the two
# given integer values are equal or their sum or difference is 5.

def check(x,y):
     if (x==y) or (abs(x-y)==5) or ((x+y)==5):
          return True
     return False
x = int(input())
y = int(input())
print(check(x,y))
