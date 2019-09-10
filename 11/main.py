number = 17
run = True

while run:
    guess = int(input("Enter a number:"))
    if guess == number:
        print("yes")
        run = False
    elif guess > number:
        print("too high")
    else:
        print("too low")