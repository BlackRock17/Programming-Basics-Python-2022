needful_sum = int(input())

cash = 0
cash_person = 0
card = 0
card_person = 0
total_sum = cash + card
counter = 0

while True:
    if total_sum >= needful_sum:
        print(f"Average CS: {cash / cash_person:.2f}")
        print(f"Average CC: {card / card_person:.2f}")
        break

    product_price = input()

    if product_price == "End":
        print(f"Failed to collect required money for charity.")
        break

    price = int(product_price)
    counter += 1

    if counter % 2 == 1:
        pass



