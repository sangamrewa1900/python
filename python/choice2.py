print(".......RATE LIST.......")
print("Pen Rs of 10 ")
print("Paper Rs of 2 ")
print("pancil Rs of 5 ")
print("Eraser Rs of 7 ")
print("Book Rs of 25 ")
n = int(input("enter your choice-: "))
if n == 1 :
    p = int(input("how many pen you want to buy-: "))
    x = p*10
    print("total price of the Pen is -: " , x)
elif n==2:
    p =int(input("how many paper you want to buy -:"))
    x=p*2
    print("total price of the Paper is -: " , x)
elif n==3:
    p =int(input("how many Pancil you want to buy -:"))
    x=p*5
    print("total price of the Pancil is -: " , x)
elif n==4:
    p =int(input("how many Eraser you want to buy -:"))
    x=p*7
    print("total price of the Eraser is -: " , x)
elif n==5:
    p =int(input("how many Book you want to buy -:"))
    x=p*25
    print("total price of the Book is -: " , x)
else:
    print("wrong input")
