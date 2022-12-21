customer = int(input())

total_money_spend = 0

for i in range(0, customer):
    num_purchased = 0
    last_price = 0
    while True:
        purchase = input()

        if purchase == "Finish":
            if num_purchased % 2 == 0:
                last_price *= 0.8
            total_money_spend += last_price
            print(f"You purchased {num_purchased} items for {last_price:.2f} leva.")
            break

        elif purchase == "basket":
            last_price += 1.5
        elif purchase == "wreath":
            last_price += 3.8
        elif purchase == "chocolate bunny":
            last_price += 7

        num_purchased += 1

print(f"Average bill per client is: {total_money_spend / customer:.2f} leva.")





