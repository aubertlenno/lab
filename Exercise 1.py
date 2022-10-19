# Number Guessing Game

# import random
# lowerBound = int(input("Enter the starting number: "))
# upperBound = int(input("Enter the end number"))
# randomInt = random.randint(lowerBound,upperBound)

# print("\n// Welcome To The Number Guessing Game!! //\n")

# numberInput = ""

# while numberInput != randomInt:
#     numberInput = int(input("Please type your guess from 1-100: "))
#     if numberInput == randomInt:
#         print("Your guess was correct! Congrats!")
#         break
#     elif numberInput < randomInt and numberInput <= 100:
#         print("Your guess was too low")
#     elif numberInput > randomInt and numberInput <= 100:
#         print("Your guess was too high")
#     else:
#         print("Error!\nGuess lower than 0 or higher than 100")

firstWord = input("Kata pertama: ")
secondWord = input("Kata kedua: ")

word1 = []
word2 = []

for i in firstWord:
    word1.append(i)

for j in secondWord:
    word2.append(j)

print(range(word1))