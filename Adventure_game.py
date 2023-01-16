name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are in a spooky area searching for the way out.would you like to take left or right? ").lower()

if answer == "left":
    answer = input(
        "Entered in to a room and got a torch!.would you like to switch on the torch or not (on/off) ").lower()

    if answer == "on":
        print("YOU SAW A GHOST AND GOT POSSESSED!! ")
    elif answer == "off":
        print("you tripped into a sharp knife and died.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a room entrance door, it looks shabby, do you want to pass it or head back (pass/back)? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "pass":
        answer = input(
            "You pass the room and meet a stranger. Do you want to talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stanger and they give you map to find a way out. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they got offended and murdered you!!.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
