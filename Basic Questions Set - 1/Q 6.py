# 6. Write a Python program which accepts a sequence of
# comma-separated numbers from user and generate a list
# and a tuple with those numbers.

a=input("Enter comma-separated numbers : ").split(',')
print("List : {}".format(list(a)))
print("Tuple : {}".format(tuple(a)))
