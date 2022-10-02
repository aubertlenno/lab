# Number Guessing Game

import random
randomInt = random.randint(1,100)

numberInput = ""

while numberInput != randomInt:
    numberInput = int(input("Please type your guess from 1-100: "))
    if numberInput == randomInt:
        print("Your guess was correct! Congrats!")
        break
    elif numberInput < randomInt and numberInput <= 100:
        print("Your guess was too low")
    elif numberInput > randomInt and numberInput <= 100:
        print("Your guess was too high")
    else:
        print("Error!\nGuess lower than 0 or higher than 100")