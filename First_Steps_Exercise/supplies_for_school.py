packages_pens = int(input())
packages_markers = int(input())
liters_of_detergent = int(input())
percent_discount = int(input()) / 100

price_pens = 5.80
price_markers = 7.20
price_detergent = 1.20

price_before_discount = (price_pens * packages_pens) + (price_markers * packages_markers) + \
                        (price_detergent * liters_of_detergent)

total = price_before_discount - (price_before_discount * percent_discount)

print(total)
