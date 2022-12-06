type_flowers = input()
num_flowers = int(input())
budget = int(input())

rose = 5
dahlia = 3.8
tulip = 2.8
narcissus = 3
gladiolus = 2.5
price = 0

if type_flowers == "Roses":
    price = num_flowers * rose
    if num_flowers > 80:
        price *= 0.9
elif type_flowers == "Dahlias":
    price = num_flowers * dahlia
    if num_flowers > 90:
        price *= 0.85
elif type_flowers == "Tulips":
    price = num_flowers * tulip
    if num_flowers > 80:
        price *= 0.85
elif type_flowers == "Narcissus":
    price = num_flowers * narcissus
    if num_flowers < 120:
        price *= 1.15
elif type_flowers == "Gladiolus":
    price = num_flowers * gladiolus
    if num_flowers < 80:
        price *= 1.2

if budget >= price:
    print(f"Hey, you have a great garden with {num_flowers} {type_flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
