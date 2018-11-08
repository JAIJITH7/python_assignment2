#25. Implement a function to count the number of vowels present in the file. 

f =open ("text.txt","r")
f1=f.read()
vowels = 0
for i in f1:
	for ch in i:
		if (i =='a' or i == 'e' or i == 'i' or i == 'o' or i== 'u' or i == 'A' or i== 'E' or i== 'O' or i=='I' or i=='U'):
			vowels = vowels + 1
print(vowels)
