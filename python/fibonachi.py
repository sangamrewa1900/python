a=0
b=1
n=int(input("Enter the limit:-"))
print(a)
print(b)
for d in range(2,n): 
	c=a+b
	print(c)
	a,b=b,c
