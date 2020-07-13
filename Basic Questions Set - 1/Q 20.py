# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def new_str(s,num):
    r=""
    for i in range(n):
        r+=s
    return r
a=input("Enter a string : ")
n=int(input("No. of copies : "))
print("Result : ")
print(new_str(a,n))
