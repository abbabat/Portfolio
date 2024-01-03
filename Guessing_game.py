import random

print("$# Welcome to the guessing game &#")

guess = random.randint(1 , 10)


while True:
    your_Guess = int(input("please enter a number between 1 and 10: "))
    if your_Guess == guess:
        print("Congratulation, you guessed right!")
        break
    elif your_Guess > guess:
        print("A lower numer !")
    elif your_Guess< guess:
        print("A higher numer !")
