# 2. Write a Python program to get the Python version you are using.
# 3. Write a Python program to display the current date and time.

import sys

print("Version Info : ")
print(sys.version)
print(sys.version_info)

import datetime

dt=datetime.datetime.now()
dt=str(dt).split()
print("Current Date : ")
print(dt[0])
print("Current Time : ")
print(dt[1])
