#Implement a program using CLA for simple arithmetic calculator exmaple: operand operator operand ie. 10 + 10 / 30 * 20

import sys


a=float(sys.argv[1])
b=(sys.argv[2])
c=float(sys.argv[3])


if b=='+':
	sum=a+c
	print(sum)
	
elif b=='-':
	sub=a-c
	print(sub)
	
elif b=='*':
	multiple=a*c
	print(multiple)
	
elif b=='/':
	div=a/c
	print(div)

else:
	print("invalid input")
	


