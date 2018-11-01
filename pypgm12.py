# Implement a program with lamda functions, for finding the area of circle, triangle, square.

x = lambda pi, r : pi * r * r
print("the area of circle=\n")
print(x(3.142, 2)) 

tri=lambda a,b,h : a*b*h
print("the area of triangle=\n")
print(tri(0.5,2,2))

sq=lambda l : l*l
print("the area of square=\n")
print(sq(2))
