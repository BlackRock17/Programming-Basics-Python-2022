coins_one = int(input())
coins_two = int(input())
coins_five = int(input())
sum = int(input())

for one in range(coins_one + 1):
    for two in range(coins_two + 1):
        for five in range(coins_five + 1):

            if (one * 1) + (two * 2) + (five * 5) == sum:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {sum} lv.")


