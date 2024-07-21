print('''enter your choice-:
press 1 for pen 
press 2 for paper
press 3 for pancil
press 4 for eraser
press 5 for book''')
num=0
n= int(input("enter your choice-:"))
if n==1:
    num=int(input("how many pen you want to buy-:"))
    total=num*10
elif n==2:
    num=int(input("how many paper you want to buy-:"))
    total=num*2
elif n==3:
    num=int(input("how many pancil you want to buy-:"))
    total=num*5
elif n==4:
    num=int(input("how many eraser you want to buy-:"))
    total=num*8
elif n==5:
    num=int(input("how many book you want to buy-:"))
    total=num*25

n=(input("Do you want to countinue shoping-:"))
while n=='yes':
    n= int(input("enter your choice-:"))
    if n==1:
        num=int(input("how many pen you want to buy-:"))
        total=num*10    
    elif n==2:
        num=int(input("how many paper you want to buy-:"))
        total=num*2
    elif n==3:
        num=int(input("how many pancil you want to buy-:"))
        total=num*5
    elif n==4:
        num=int(input("how many eraser you want to buy-:"))
        total=num*8
    elif n==5:
        num=int(input("how many book you want to buy-:"))
        total=num*50
    n=(input("Do you want to countinue shoping-:"))

else:
    print("thank_you😊")   

print("your total amount is " ,total ,'Rs')
sgst=8/100*total
cgst=8/100*total
print("sgst is",sgst)
print("and cgst is",cgst)
if total<500:
    print("delevry charge 50")
    dele=50
else:
    print("no delevry charge's")
    dele =0
full=total+sgst+cgst+dele
print("your total bill is " ,full)
    
    
