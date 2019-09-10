from random import randint

number = randint(0, 9)
while True:
    userGuess = int(input("Guess a number: "))
    if number == userGuess:
        print("Correct guess!")
        break
    print("Unlucky, try again")
