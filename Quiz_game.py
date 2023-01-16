print("Welcome to quiz game")

playing = input("Do you want to play: ")

if playing.lower() != 'yes':
    quit()

score = 0

print("Lets play :)")

Answer = input("What is the full form of CPU? ")
if Answer.lower() == 'central processing unit':
    print("correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("What is the full form of AI? ")
if Answer.lower() == 'artificial intelligence':
    print("correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("What is the full form of html? ")
if Answer.lower() == 'hyper text markup language':
    print("correct!")
    score += 1
else:
    print("Incorrect!") 

Answer = input("What is the full form of css? ")
if Answer.lower() == 'cascading style sheet':
    print("correct!")
    score += 1
else:
    print("Incorrect!")    


print('you have got ' +str(score)+ ' Questions correct!')

print('with ' +str((score/4)*100)+ '%.')

