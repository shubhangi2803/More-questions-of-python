# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

a,b=map(float,input("Enter first coordinates : ").split(','))
c,d=map(float,input("Enter second coordinates : ").split(','))
d=((a-c)**2+(b-d)**2)**(0.5)
print("Distance : {}".format(d))
