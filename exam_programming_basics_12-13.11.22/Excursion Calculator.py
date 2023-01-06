people = int(input())
season = input()

total_sum = 0

if season == "spring":
    if people <= 5:
        total_sum = people * 50
    else:
        total_sum = people * 48

elif season == "summer":
    if people <= 5:
        total_sum = people * 48.5 * 0.85
    else:
        total_sum = people * 45 * 0.85

elif season == "autumn":
    if people <= 5:
        total_sum = people * 60
    else:
        total_sum = people * 49.5

elif season == "winter":
    if people <= 5:
        total_sum = people * 86 * 1.08
    else:
        total_sum = people * 85 * 1.08

print(f"{total_sum:.2f} leva.")
