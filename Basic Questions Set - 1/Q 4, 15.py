# 4. Write a Python program which accepts the radius of a circle
# from the user and compute the area.

# 15. Write a Python program to get the volume of a sphere with radius 6.

import math

radius=float(input("Enter radius of circle : "))
print("Area : {}".format(math.pi*radius*radius))

rad=float(input("Enter radius of sphere : "))
print("Volume : {}".format((4/3)*math.pi*rad*rad*rad))
