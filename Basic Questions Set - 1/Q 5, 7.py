# 5. Write a Python program which accepts the user's first and last
# name and print them in reverse order with a space between them.
# 7. Write a Python program to accept a filename from the user
# and print the extension of that. 

fname=input("Enter first name : ")
lname=input("Enter last name : ")
print("{} {}".format(lname,fname))

file=input("Enter file : ")
x=file.split('.')[1]
print("Extension : {}".format(x))
