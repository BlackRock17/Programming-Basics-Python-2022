fats = int(input())
protein = int(input())
carbohydrates = int(input())
calories = int(input())
percent_water = int(input())

total_fats = (fats / 100 * calories) / 9
total_protein = (protein / 100 * calories) / 4
total_carbo = (carbohydrates / 100 * calories) / 4

total_food = total_fats + total_protein + total_carbo

calories_1gm = (calories / total_food)

calories_1gm -= (calories_1gm / 100 * percent_water)


print(f"{calories_1gm:.4f}")
