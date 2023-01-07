days = int(input())

total_liters = 0
total_degrees = 0

for i in range(0, days):
    quantity = float(input())
    degrees = float(input())

    total_liters += quantity
    total_degrees += quantity * degrees

final_degrees = total_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {final_degrees:.2f}")

if final_degrees < 38:
    print("Not good, you should baking!")
elif final_degrees > 42:
    print("Dilution with distilled water!")
else:
    print("Super!")
