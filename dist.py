#  Implement a python program to find distance between two point.

from math import sqrt

x1=int(input("enter point x1 in (x1,y1): "))
x2=int(input("enter point x2 in (x2,y2): "))
y1=int(input("enter point y1 in (x1,y1): "))
y2=int(input("enter point y2 in (x2,y2): "))
d=sqrt(((x2-x1)**2)+((y2-y1)**2))
print("the distance between two points are: ",d)
