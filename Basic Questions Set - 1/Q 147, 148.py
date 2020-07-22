# 147. Write a Python function to check whether a number is divisible by another number.
#      Accept two integers values form the user.
# 148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
#      Note: Do not use built-in functions.

print("To check if one number is divisible by another number")
x=int(input("Enter number to be checked : "))
y=int(input("Give the other number : "))
if x%y==0:
    print("{} is divisible by {}".format(x,y))
else:
    print("Not divisible")

print("To find maximum and minimum from a sequence of numbers")
li=list(map(int,input("Enter sequence of numbers : ").split()))
maxi=None
maxpos=None
mini=None
minipos=None
i=1
for num in li:
    if maxi is None or maxi<num:
        maxi=num
        maxipos=i
    if mini is None or mini>num:
        mini=num
        minipos=i
    i+=1
print("Minimum value is : {} at {} position".format(mini,minipos))
print("Maximum value is : {} at {} position".format(maxi,maxipos))

        
        
