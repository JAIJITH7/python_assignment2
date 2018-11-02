#Implement a menu based  program for Arithemetic Calculator

a=int(input("enter first num : "))
b=int(input("enter second num : "))
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice=input("enter choice 1/2/3/4 : ")
add=a+b
sub=a-b
mul=a*b
div=a/b
if choice==1:
	print(add)
elif choice==2:
	print(sub)
elif choice==3:
	print(mul)
elif choice==4:
	print(div)
else:
	print("invalid input")	
