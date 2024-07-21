num = int(input("enter the value..."))
n=num
rev =0
while num>0:
    x = num%10
    rev=rev*10+x
    num=int(num/10)
if n==rev:
    print("this is pallendrom")
else:
    print("this is not pallendrom")
