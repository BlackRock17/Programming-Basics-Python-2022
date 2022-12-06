nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5
bags_price = 0.40

nylon += 2
paint += paint * 0.10

material_price = (nylon_price * nylon) + (paint_price * paint) + \
                 (thinner_price * thinner) + (bags_price * 1)
price_for_one_hour_work = material_price * 0.30

total = material_price + (price_for_one_hour_work * hours)

print(total)
