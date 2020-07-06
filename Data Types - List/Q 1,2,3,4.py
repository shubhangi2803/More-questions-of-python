# 1. Write a Python program to sum all the items in a list.
# 2. Write a Python program to multiplies all the items in a list.
# 3. Write a Python program to get the largest number from a list.
# 4. Write a Python program to get the smallest number from a list.

li=list(map(int,input("Enter list elements separated by space : ").split()))

sum_list=0
multiply=1
small=None
large=None

for num in li:
    sum_list+=num
    multiply*=num
    if large is None or large<num:
        large=num
    if small is None or small>num:
        small=num

print("Sum of list : {}".format(sum_list))
print("All list elements multiplied give : {}".format(multiply))
print("Largest number : {}".format(large))
print("Smallest numbe : {}".format(small))

# Using in-built functions:
#  sum_list=sum(li)
#  large=max(li)
#  small=min(li)
