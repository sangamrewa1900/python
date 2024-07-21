n = int(input("enter the value-:"))
total =0
while n>0:
    r=n%10
    total=total+r 
    n=n//10
print("the total sum of digits " ,total)
