#31. Implement a program to check the elements of a list is a palindrome or not.
num = raw_input("enter the number:")
if ( num==num[::-1]):
	print("number is palindrome")
else:
	print("number is not palindrome")

