cost = 2

received = int(input("Insert money: "))

if received < cost:
    print("Insert more money")
else:
    change = received - cost
    if change > 0:
        print(f"Change given {change}")
    else:
        print("No change needed")
