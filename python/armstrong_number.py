n= int(input("enter the number.."))
temp=n
add=0
while temp!=0:
    k =temp%10
    add +=k*k*k
    temp=int(temp/10)
if add == n:
    print("given number is Armstrong Number")
else:
    print("Given number is not Armstrong Number")
