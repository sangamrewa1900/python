l=[]
print(l)
n = int(input("how many numbers you want to insert.."))
for a in range(n):
    l.append(int(input("enter the value..")))
print(l)
m=l[0]
for a in range(len(l)):
            if m<l[a]:
                    m=l[a]
print("max value is ",m)
