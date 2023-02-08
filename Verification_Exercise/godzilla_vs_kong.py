budget = float(input())
num_statist = int(input())
prc_clothes = float(input())

decor = budget * 0.10

if num_statist > 150:
    prc_clothes *= 0.90

clothes = prc_clothes * num_statist

total_prc = decor + clothes

if total_prc > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_prc - budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - total_prc:.2f} leva left.")
