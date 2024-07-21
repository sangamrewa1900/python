l=[]
n=int(input("how many element you want to insert.."))
for a in range(n):
   l.append(int(input("Enter the value...")))
   temp = 0;
'''
for i in range(0,len(l)):    
    print(l[i], end=" ")    
for i in range(0, len(l)):    
    for j in range(i+1, len(l)):    
        if(l[i] > l[j]):    
            temp = l[i]    
            l[i] = l[j]    
            l[j] = temp         
print()       
for i in range(0, len(l)): 
    print(l[i], end=" ")
'''
l.sort()
print(l)
