walk_min = int(input())
count_walk = int(input())
calories = int(input())

burned_cal = walk_min * count_walk * 5

if calories / 2 <= burned_cal:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_cal}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_cal}.")

