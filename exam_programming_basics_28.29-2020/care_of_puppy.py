food_kg = int(input()) * 1000

while True:
    command = input()

    if command == "Adopted":
        break

    food_eaten = int(command)

    food_kg -= food_eaten

if food_kg >= 0:
    print(f"Food is enough! Leftovers: {food_kg} grams.")
else:
    print(f"Food is not enough. You need {abs(food_kg)} grams more.")


