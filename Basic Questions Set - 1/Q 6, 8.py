# 6. Write a Python program which accepts a sequence of
# comma-separated numbers from user and generate a list
# and a tuple with those numbers.

# 8. Write a Python program to display the first and
# last colors from the following list.

a=input("Enter comma-separated numbers : ").split(',')
print("List : {}".format(list(a)))
print("Tuple : {}".format(tuple(a)))

b=input("Enter list of colors : ").split()
print("First color : {}".format(b[0]))
print("Last color : {}".format(b[-1]))
