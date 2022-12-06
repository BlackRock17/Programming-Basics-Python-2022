import math

num_magnolias = int(input())
num_hyacinths = int(input())
num_roses = int(input())
num_cacti = int(input())
prc_gift = float(input())

magnolias = 3.25
hyacinths = 4
rose = 3.50
cacti = 8

total = (num_magnolias * magnolias) + (num_hyacinths * hyacinths) + (num_cacti * cacti) + (num_roses * rose)
total_after_taxes = total * 0.95

if total_after_taxes >= prc_gift:
    print(f"She is left with {math.floor(total_after_taxes - prc_gift)} leva.")
else:
    print(f"She will have to borrow {math.ceil(prc_gift - total_after_taxes)} leva.")
