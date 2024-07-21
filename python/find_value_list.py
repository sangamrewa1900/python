l=[]
n =int(input("how many number you want to print--"))
for a in range(n):
    l.append(int(input("enter the value--")))
print(l)
s=int(input("enter the value you want to search"))
if l.count (s)>0:
    print('value is available...')
else:
    print('value not available...')
    

