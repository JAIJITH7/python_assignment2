#Implement a program to write a line from the console to a file.

import sys
f=open("test.txt\n","a+")
a=sys.argv[1]
b=sys.argv[2]
f.write(a)
f.write(b)
print(a,b)
