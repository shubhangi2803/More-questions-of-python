# 5.Write a Python program to calculate surface volume and area of a cylinder.
# 6.Write a Python program to calculate surface volume and area of a sphere.
import math as m
pi=m.pi
print("CYLINDER")
ht=float(input("Height : "))
cy_radius=float(input("Radius : "))
cy_sa=(2*pi*cy_radius*ht)+(2*pi*cy_radius*cy_radius)
cy_vol=pi*cy_radius*cy_radius*ht
print("Surface Area : {}".format(cy_sa))
print("Volume : {}".format(cy_vol))

print("SPHERE")
radius=float(input("Radius : "))
sp_sa=4*pi*radius*radius
sp_vol=(4/3)*pi*radius*radius*radius
print("Surface Area : {}".format(sp_sa))
print("Volume : {}".format(sp_vol))
