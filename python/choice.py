print("press 1 for addition-: ")
print("press 2 for substration-: ")
print("press 3 for multiplication-: ")
print("press 4 for divition-: ")
n = int(input("enter your choice :"))
if n==1:
    num1 = int(input("enter 1st num...."))
    num2 = int(input("enter 2nd num...."))
    print("total is " , num1+num2)
elif n==2:
    num1 = int(input("enter 1st num...."))
    num2 = int(input("enter 2nd num...."))
    print("total is " , num1-num2)
elif n==3:
    num1 = int(input("enter 1st num...."))
    num2 = int(input("enter 2nd num...."))
    print("total is " , num1*num2)
elif n==4:
    num1 = int(input("enter 1st num...."))
    num2 = int(input("enter 2nd num...."))
    print("total is " , num1/num2)
else:
    print("wrong input")
