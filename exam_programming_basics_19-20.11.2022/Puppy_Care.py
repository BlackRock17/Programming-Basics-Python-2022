food = int(input()) * 1000

total_eaten = 0

while True:
    food_eaten = input()

    if food_eaten == "Adopted":
        if food >= total_eaten:
            print(f"Food is enough! Leftovers: {food - total_eaten} grams.")
        else:
            print(f"Food is not enough. You need {total_eaten - food} grams more.")
        break

    food_gr = int(food_eaten)

    total_eaten += food_gr

