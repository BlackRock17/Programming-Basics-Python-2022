type_of_fuel = input()
quantity = float(input())
club_card = input()

petrol_prc = 2.22
diesel_prc = 2.33
gas_prc = 0.93

total = 0

if type_of_fuel == "Gasoline":
    total = quantity * petrol_prc
    if club_card == "Yes":
        total = total - (quantity * 0.18)

if type_of_fuel == "Diesel":
    total = quantity * diesel_prc
    if club_card == "Yes":
        total = total - (quantity * 0.12)

if type_of_fuel == "Gas":
    total = quantity * gas_prc
    if club_card == "Yes":
        total = total - (quantity * 0.08)

if quantity >= 20 and quantity <= 25:
    total = total * 0.92
elif quantity > 25:
    total = total * 0.90

print(f"{total:.2f} lv.")
