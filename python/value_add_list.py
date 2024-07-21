i=[]
print(i)
n= int(input("how many numbers you want to insert..."))
for a in range(n):
    i.append(int(input("enter the value...")))
print(i)
s=0
for a in range(len(i)):
    s=s+i[a]
print(s)
