val1 = int(input("enter 1st value"))
val2 = int(input("enter 2nd value"))
val3 = int(input("enter 3rd value"))

if val1>val2:
    if val1>val3:
        print("first number is biggest")
    else:
        print("third number is biggest")
else:
    if val2>val3:
        print("second number is biggest")
    else:
        print("third number is biggest")
