#Distance between centers C1 and C2 is calculated as
 #C1C2 = sqrt((x1 - x2)2 + (y1 - y2)2).
#There are three condition arises.
#1. If C1C2 == R1 + R2
     #Circle A and B are touch to each other.
#2. If C1C2 > R1 + R2
     #Circle A and B are not touch to each other.
#3. If C1C2 < R1 + R2
      #Circle intersects each other.

from math import sqrt

x1=int(input("enter point x1 in (x1,y1): "))
x2=int(input("enter point x2 in (x2,y2): "))
y1=int(input("enter point y1 in (x1,y1): "))
y2=int(input("enter point y2 in (x2,y2): "))
d=sqrt(((x2-x1)**2)+((y2-y1)**2))
r1=int(input("enter radius of circle one: "))
r2=int(input("enter radius of circle two: "))
r=r1+r2
if d==r:
	print("two circles touch each other ")
elif d>r:
	print("two circles do not touch each other ")
else:
	print("circles intersects each other ")	
