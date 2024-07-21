l=[[1,2,3],[4,5,6],[7,8,9]]
for a in range(len(l)):
    print(a)
    m=l[0]
for a in range(len(l)):
    if m<l[a]:
        m=l[a]
print("max",m)
