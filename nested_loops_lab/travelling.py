while True:
    destination = input()
    saving_money = 0

    if destination == "End":
        break

    budget = float(input())

    while True:
        money = float(input())
        saving_money += money

        if saving_money >= budget:
            print(f"Going to {destination}!")
            break


