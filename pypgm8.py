 #Implement a program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately. 
 
tuple1=('apple','mango','banana')
tuple2=('potato','tomato','brinjal')
list1=list(zip(tuple1,tuple2))
print(list1)

for i in list1:
	print(tuple1)
	
for i in list1:
	print(tuple2)
	
	
