trunk_capacity = float(input())

suitcase_counter = 0

while trunk_capacity > 0:
    suitcase_bulk = input()
    if suitcase_bulk == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    suitcase = float(suitcase_bulk)
    suitcase_counter += 1

    if suitcase_counter % 3 == 0:
        suitcase *= 1.1

    if suitcase > trunk_capacity:
        suitcase_counter -= 1
        print("No more space!")
        break

    trunk_capacity -= suitcase

print(f"Statistic: {suitcase_counter} suitcases loaded.")


