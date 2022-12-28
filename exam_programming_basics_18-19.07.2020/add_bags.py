prc_luggage = float(input())
kg_luggage = float(input())
days_until_fly = int(input())
num_luggage = int(input())

if kg_luggage < 10:
    prc_luggage *= 0.2
elif 10 <= kg_luggage <= 20:
    prc_luggage *= 0.5

if days_until_fly > 30:
    prc_luggage *= 1.1
elif 30 >= days_until_fly >= 7:
    prc_luggage *= 1.15
elif days_until_fly < 7:
    prc_luggage *= 1.4

print(f" The total price of bags is: {prc_luggage * num_luggage:.2f} lv. ")
