total_sum = 0

while True:
    amound_received = input()
    if amound_received == "NoMoreMoney":
        break

    money = float(amound_received)

    if money < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {money:.2f}")
    total_sum += money

print(f"Total: {total_sum:.2f}")

