from minibus import calculateMinibusNeeded

minibuses = int(input("How many minibuses are available? "))

seatsPerMinibus = int(input("how many seats per minibus? "))

pupils = int(input("How many people are going on the trip? "))

needed = calculateMinibusNeeded(minibuses, seatsPerMinibus, pupils)

if needed != 0:
    print(f"we need {needed} more minibuses")
else:
    print("we have enough seats")
