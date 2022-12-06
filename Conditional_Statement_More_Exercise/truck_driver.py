season = input()
km_month = float(input())

total_prc = 0

if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        total_prc = km_month * 0.75
    elif season == "Summer":
        total_prc = km_month * 0.9
    elif season == "Winter":
        total_prc = km_month * 1.05

elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        total_prc = km_month * 0.95
    elif season == "Summer":
        total_prc = km_month * 1.1
    elif season == "Winter":
        total_prc = km_month * 1.25

else:
    total_prc = km_month * 1.45

print(f"{total_prc * 4 * 0.9:.2f}")

