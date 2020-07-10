# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.
li=list(map(int,input("Enter list of numbers : ").split()))
p=list(map(lambda x: x*x, li))
q=list(map(lambda y: y*y*y, li))
print("List of squares : {}".format(p))
print("List of cubes : {}".format(q))
