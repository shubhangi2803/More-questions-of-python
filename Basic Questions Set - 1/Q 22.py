# 22. Write a Python program to count the number 4 in a given list.

li=list(map(int,input().split()))
p=list(filter(lambda x:x==4,li))
print("Number of 4's : {}".format(len(p)))
