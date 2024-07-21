l=[]
print(l)
n= int(input("how many value you want to enter.."))
for a in range(n):
    l.append(int(input("enter any value..")))
print(l)
s=0
for a in range(len(l)):
    s=s+l[a]
print(s)
