import sys
def exit_game():
    print("Invalid choice, Exit the game!")
    sys.exit()

print("Welcome to the adventureGame")
print("How can I call you? ")
player_name = input("Name: ")
print("Please, choose your vehicle: car or motocycle ")
vehicle = input("The vehicle is: ")
if(vehicle=="car"):
    toll_fee = 5
elif(vehicle=="motocycle"):
    toll_fee = 3
else:
    exit_game()
extra_gas = 0
total_pay = 0 
pre_pay = 10
print("Welcome " + player_name + " .you are in the road. Now, you have to choose the direction to go.")
choice = input("(left or right): ")
if(choice=="left"):
    print("You now have to pay for the toll")
    if(vehicle=="car"):
            extra_gas = -2
            total_pay = extra_gas + toll_fee+pre_pay
            print("Your total fee is "+ str(total_pay))
    elif(vehicle=="vehicle"):
           extra_gas = -1
           total_pay = extra_gas + toll_fee+ pre_pay
           print("your total is "+ str(total_pay))
    else: exit_game()
elif(choice=="right"):
    print("You now do not have to pay for the toll")
    if(vehicle=="car"):
            extra_gas = 2
            toll_fee =0
            total_pay = extra_gas + toll_fee+pre_pay
            print("your total is "+ str(total_pay))
    elif(vehicle=="motocycle"):
           extra_gas = 1
           toll_fee = 0
           total_pay = extra_gas + toll_fee+ pre_pay 
           print("your total : "+ str(total_pay))
    else: exit_game()
else:
    exit_game()
