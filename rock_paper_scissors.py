import random

computer_win=0
user_win=0

options=["rock","paper","scissors"]

while True:
    user_input=input("Type rock/paper/scissor or q for quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number=random.randint(0,2)    
    computer_choice=options[random_number]
    print("computer_choose " ,computer_choice+".")
    
    if user_input== "rock" and computer_choice == "scissors":
        print("You Won")
        user_win += 1
    elif user_input== "paper" and computer_choice == "rock":
        print("You Won")
        user_win += 1
    elif user_input== "scissors" and computer_choice == "paper":
        print("You Won")
        user_win += 1
    else:
        print("you lose!!")
        computer_win += 1
        
print("You won" , user_win , "times.")
print("The computer won" , computer_win , "times.")
print("Thank you :)")