# 3.Write a Python program to calculate the area of a trapezoid.
# 4.Write a Python program to calculate the area of a parallelogram. 

print("Area of trapezoid,i.e, trapezium with equal base angles")
tr_ht=float(input("Height : "))
tr_base1=float(input("Base 1 : "))
tr_base2=float(input("Base 2 : "))
tr_area=0.5*(tr_base1+tr_base2)*tr_ht
print("Area : {}".format(tr_area))
print("Area of parallelogram")
pr_ht=float(input("Height : "))
pr_base=float(input("Base : "))
pr_area=pr_ht*pr_base
print("Area : {}".format(pr_area))
