n = int(input("enter day -:"))
if n<=31:

    if n%7==1:
        print("day is monday")
    elif n%7==2:
        print("day is tuesday")
    elif n%7==3:
        print("day is wednesday")
    elif n%7==4:
        print("day is thursday")
    elif n%7==5:
        print("day is friday")
    elif n%7==6:
        print("day is saturday ")
    elif n%7==0:
        print("day is sunday")
else:
      print("wrong day")
