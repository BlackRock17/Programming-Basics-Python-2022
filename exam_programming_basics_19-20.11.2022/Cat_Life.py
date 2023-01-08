import math

cat_breed = input()
gender = input()

months = 0

if cat_breed == "British Shorthair":
    if gender == "m":
        months += 13 * 2
    elif gender == "f":
        months += 14 * 2
elif cat_breed == "Siamese":
    if gender == "m":
        months += 15 * 2
    elif gender == "f":
        months += 16 * 2
elif cat_breed == "Persian":
    if gender == "m":
        months += 14 * 2
    elif gender == "f":
        months += 15 * 2
elif cat_breed == "Ragdoll":
    if gender == "m":
        months += 16 * 2
    elif gender == "f":
        months += 17 * 2
elif cat_breed == "American Shorthair":
    if gender == "m":
        months += 12 * 2
    elif gender == "f":
        months += 13 * 2
elif cat_breed == "Siberian":
    if gender == "m":
        months += 11 * 2
    elif gender == "f":
        months += 12 * 2

if months != 0:
    print(f"{math.floor(months)} cat months")
else:
    print(f"{cat_breed} is invalid cat!")







