num_cats = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
total_food = 0

for i in range(0, num_cats):
    food = float(input())

    total_food += food

    if 100 <= food < 200:
        group_1 += 1
    elif 200 <= food < 300:
        group_2 += 1
    elif 300 <= food <= 400:
        group_3 += 1

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {total_food / 1000 * 12.45:.2f} lv.")


