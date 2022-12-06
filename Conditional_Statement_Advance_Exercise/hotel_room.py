month = input()
nights = int(input())

studio_prc = 0
apartment_prc = 0

if month == "May" or month == "October":
    studio_prc = nights * 50
    apartment_prc = nights * 65
    if nights > 14:
        studio_prc *= 0.70
    elif nights > 7:
        studio_prc *= 0.95
elif month == "June" or month == "September":
    studio_prc = nights * 75.2
    apartment_prc = nights * 68.7
    if nights > 14:
        studio_prc *= 0.8
elif month == "July" or month == "August":
    studio_prc = nights * 76
    apartment_prc = nights * 77

if nights > 14:
    apartment_prc *= 0.9

print(f"Apartment: {apartment_prc:.2f} lv.")
print(f"Studio: {studio_prc:.2f} lv.")
