money_for_excursion = float(input())
available_money = float(input())

days = 0
saved_money = available_money
counter = 0

while saved_money <= money_for_excursion:
    action = input()
    sum = float(input())

    if action == "spend":
        saved_money -= sum
        counter += 1
        days += 1
        if saved_money < 0:
            saved_money = 0
        if counter == 5:
            print("You can't save the money.")
            print(days)
            break

    if action == "save":
        saved_money += sum
        counter = 0
        days += 1
        if saved_money >= money_for_excursion:
            print(f"You saved the money for {days} days.")
            break
