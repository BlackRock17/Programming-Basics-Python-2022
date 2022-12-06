money = float(input())
years = int(input())

Ivancho_age = 17
money_left = money

for i in range(1800, years + 1):
    Ivancho_age += 1

    if i % 2 == 0:
        money_left -= 12000

    else:
        money_left -= 12000 + (Ivancho_age * 50)

if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")
