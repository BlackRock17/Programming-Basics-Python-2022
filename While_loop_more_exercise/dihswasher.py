detergent = int(input()) * 750

washed_dishes = 0
washed_pots = 0
counter = 0

while True:
    utensils = input()

    if utensils == "End":
        print("Detergent was enough!")
        print(f"{washed_dishes} dishes and {washed_pots} pots were washed.")
        print(f"Leftover detergent {detergent} ml.")
        break

    count_dishes = int(utensils)
    counter += 1

    if counter % 3 == 0:
        washed_pots += count_dishes
        detergent -= count_dishes * 15
        if detergent < 0:
            print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
            break

    else:
        washed_dishes += count_dishes
        detergent -= count_dishes * 5
        if detergent < 0:
            print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
            break
