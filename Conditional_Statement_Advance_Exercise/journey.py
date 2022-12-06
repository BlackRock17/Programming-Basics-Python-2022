budget = float(input())
season = input()
kind_of_vacation = ""
price = 0
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        kind_of_vacation = "Camp"
        price = budget * 0.3
    elif season == "winter":
        kind_of_vacation = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        kind_of_vacation = "Camp"
        price = budget * 0.4
    elif season == "winter":
        kind_of_vacation = "Hotel"
        price = budget * 0.8
else:
    destination = "Europe"
    kind_of_vacation = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{kind_of_vacation} - {price:.2f}")

