# 5. Write a Python program to count the number of strings where
# the string length is 2 or more and the first and last character
# are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

li=list(input("Enter strings separated by spaces : ").split())
count=0
for string in li:
    if len(string)>=2 and string[0]==string[-1]:
        count+=1
print("Result : {}".format(count))
