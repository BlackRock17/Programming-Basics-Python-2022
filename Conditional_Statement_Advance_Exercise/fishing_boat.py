budget = int(input())
season = input()
fisher = int(input())
price = 0

if season == "Spring":
    price = 3000
elif season == "Winter":
    price = 2600
elif season == "Summer" or season == "Autumn":
    price = 4200

if fisher <= 6:
    price *= 0.9
elif 7 <= fisher <= 11:
    price *= 0.85
else:
    price *= 0.75

if fisher % 2 == 0 and season != "Autumn":
    price *= 0.95

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
