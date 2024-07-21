print(''' 1 for add a car-: 
 2 for add a bike-: 
 3 for Remove a car-: 
 4 for Remove a bike-: 
 5 for total num. of car-:
 6 for total number of bike-:''')
max_car = 50
max_bike = 30
no_of_car = 0
no_of_bike = 0
num = int(input("enter your choice-: "))
if num ==1:
    car = int(input("how many cars  you want to park:- "))
    if car<=max_car:
        max_car = max_car-car
        no_of_car = no_of_car+car
        print("car park Sucessfully...")
    else:
        print("We don't have space")

elif num ==2:
    bike =int(input("how many bikes you want to park:-"))
    if bike<=max_bike:
        max_bike = max_bike-bike
        no_of_bike = no_of_bike+bike
        print("bike park sucessfully...")
    else:
        print("we don't have space")
elif num == 3:
    car =int(input("how many car's you want to remove..."))
    if rem_car<=no_of_car:
        max_car=max_car+rem_car
        no_of_car=no_of_car-rem_car
        print("car Remove Sucessfully...")
    else:
        print("we Don't have any car")
elif num ==4:
    bike =int(input("How many bike's you want to remove..."))
    if rem_bike <= no_of_bike:
        max_bike = max_bike+rem_bike
        no_of_bike= no_of_bike - rem_bike
        print("bike Remove Sucessfuully...")
    else:
        print("We don't have any bike")
elif num==5:
	print("total no of car is ",max_car)
elif num==6:
	print("total no of bike is ",max_bike)
    
else:
    print("wrong input")
    
