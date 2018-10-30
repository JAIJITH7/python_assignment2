# Implement a python code for arithmetic calculator for operation *, / , + , -

a=int(input("enter num1: "))
b=int(input("enter num2: "))
choice=input("enter your choice  + - * / to calculate: ")
add=a+b
sub=a-b
mul=a*b
div=a/b
if choice=='+':
	print(add)
elif choice=='-':
	print(sub)
elif choice=='*':
    print(mul)
else:
	print(div)    	