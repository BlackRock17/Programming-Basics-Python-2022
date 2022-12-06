import math

sq_m_vineyard = int(input())
grapes_1sq_m = float(input())
wine_need_lts = int(input())
num_workers = int(input())

total_qrapes = sq_m_vineyard * grapes_1sq_m
total_qrapes = total_qrapes * 0.40
total_wine = total_qrapes / 2.5

if total_wine < wine_need_lts:
    lacking_wine = wine_need_lts - total_wine
    print(f"It will be a tough winter! More {math.floor(lacking_wine)} liters wine needed.")
elif total_wine >= wine_need_lts:
    wine_left = total_wine - wine_need_lts
    wine_for_person = wine_left / num_workers
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_for_person)} liters per person.")
