sum = int(input())

cash = 0
cash_person = 0
card = 0
card_person = 0
total_sum = 0
counter = 0

while True:
    product_price = input()

    if product_price == "End":
        print(f"Failed to collect required money for charity.")
        break

    payment = int(product_price)
    counter += 1

    if counter % 2 == 1:
        if payment > 100:
            print("Error in transaction!")
        else:
            cash += payment
            total_sum += payment
            cash_person += 1
            print("Product sold!")
            if total_sum >= sum:
                print(f"Average CS: {cash / cash_person:.2f}")
                print(f"Average CC: {card / card_person:.2f}")
                break

    else:
        if payment < 10:
            print("Error in transaction!")
        else:
            card += payment
            total_sum += payment
            card_person += 1
            print("Product sold!")
            if total_sum >= sum:
                print(f"Average CS: {cash / cash_person:.2f}")
                print(f"Average CC: {card / card_person:.2f}")
                break



