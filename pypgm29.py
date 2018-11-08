#29. In a given list find the total number of odd numbers, even numbers and their respetive sum and average.
list=[1,2,3,4,5,6,7,8,9]
print('the given list is:',list)

print(sum(list))
for i in list:
	if (i % 2 == 0):
		print("even elements are:",i)
for i in list:
	if (i % 2 != 0):
print("odd elements are:",i)
