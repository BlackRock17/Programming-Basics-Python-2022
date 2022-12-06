import math

num_days = int(input())
food = int(input())
dog_daily = float(input())
cat_daily = float(input())
turtle_daily = float(input()) * 0.001

dog_food_needed = num_days * dog_daily
cat_food_needed = num_days * cat_daily
turtle_food_needed = num_days * turtle_daily

total_food_needed = dog_food_needed + cat_food_needed + turtle_food_needed

if food >= total_food_needed:
    print(f"{math.floor(food - total_food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_needed - food)} more kilos of food are needed.")

