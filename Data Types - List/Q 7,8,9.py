# 7. Write a Python program to remove duplicates from a list.
# 8. Write a Python program to check a list is empty or not.
# 9. Write a Python program to clone or copy a list.

li_one=list(map(int,input("Enter list elements separated by lists : ").split()))
li_two=[]
print("List 1 : ")
print(li_one)
print("List 2 : ")
print(li_two)

def is_empty(li):
    return len(li)==0

print("List 1 : Is Empty ?? {}".format(is_empty(li_one)))
print("List 2 : Is Empty ?? {}".format(is_empty(li_two)))

li_one_clone=li_one
li_two_clone=li_two

print("Copy of list 1 : {}".format(li_one_clone))
print("Copy of list 2 : {}".format(li_two_clone))

li_one_new=set(li_one)
print("After removing duplicates, list 1 : {}".format(li_one_new))

