# Implement a program with functions, for finding the area of circle, triangle, square.

pi=3.142
r=float(input("enter the radius to find area of circle\n"))
area=pi*r*r
print("the area of circle =",area)

b=float(input("enter the breadth of triangle\n"))
h=float(input("enter the height of triangle\n"))
areaoftri=0.5*h*b
print("the area of triangle=",areaoftri)

a=float(input("enter the side of square\n"))
areasqr=a*a
print("the area of square=",areasqr)

