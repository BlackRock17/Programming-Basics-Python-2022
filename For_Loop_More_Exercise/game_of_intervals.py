numbers = int(input())

total = 0
zero_nine = 0
ten_nineteen = 0
twenty_twentynine = 0
thirty_thirtynine = 0
fourty_fifty = 0
invalid_num = 0

for i in range(0, numbers):
    number = int(input())

    if 0 <= number <= 9:
        zero_nine += 1
        total += number * 0.2
    elif 10 <= number < 20:
        ten_nineteen += 1
        total += number * 0.3
    elif 20 <= number < 30:
        twenty_twentynine += 1
        total += number * 0.4
    elif 30 <= number < 40:
        thirty_thirtynine += 1
        total += 50
    elif 40 <= number <= 50:
        fourty_fifty += 1
        total += 100
    else:
        invalid_num += 1
        total /= 2


print(f"{total:.2f}")
print(f"From 0 to 9: {zero_nine / numbers * 100:.2f}%")
print(f"From 10 to 19: {ten_nineteen / numbers * 100:.2f}%")
print(f"From 20 to 29: {twenty_twentynine / numbers * 100:.2f}%")
print(f"From 30 to 39: {thirty_thirtynine / numbers * 100:.2f}%")
print(f"From 40 to 50: {fourty_fifty / numbers * 100:.2f}%")
print(f"Invalid numbers: {invalid_num / numbers * 100:.2f}%")
