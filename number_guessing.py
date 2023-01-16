import random

Top_of_range = input('Type a Number: ')

if Top_of_range.isdigit():
    Top_of_range= int(Top_of_range)
    if Top_of_range <= 0:
        print("Type a number larger than 0")
        quit()
else:
    print("Type a number next time")
    quit()

random_number = random.randint(0,Top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a Guess: ')
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Type a number next time")
        continue
    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You were above the Number')
    else:
        print('You were below the Number')

print('You have got it in' , guesses , 'guesses')




    