vegetable_prc_kg = float(input())
fruit_prc_kg = float(input())
vegetable_quantity = int(input())
fruit_quantity = int(input())

sum_veg = vegetable_prc_kg * vegetable_quantity
sum_fr = fruit_prc_kg * fruit_quantity

total_lv = sum_veg + sum_fr

total_eu = total_lv / 1.94

print(f"{total_eu:.2f}")
