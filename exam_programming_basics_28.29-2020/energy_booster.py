fruit = input()
size = input()
quantity = int(input())

price = 0

if fruit == "Watermelon":
    if size == "small":
        price += 2 * 56
    elif size == "big":
        price += 5 * 28.7
elif fruit == "Mango":
    if size == "small":
        price += 2 * 36.66
    elif size == "big":
        price += 5 * 19.6
elif fruit == "Pineapple":
    if size == "small":
        price += 2 * 42.1
    elif size == "big":
        price += 5 * 24.8
elif fruit == "Raspberry":
    if size == "small":
        price += 2 * 20
    elif size == "big":
        price += 5 * 15.2

price *= quantity

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.5

print(f"{price:.2f} lv.")
