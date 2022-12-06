age = int(input())
prc_wash_mash = float(input())
prc_toy = int(input())

money_taken = 0
save_money = 0
num_toys = 0
brother_taken = 0

for years in range(1, age + 1):
    if years % 2 == 0:
        money_taken += 10
        save_money += money_taken
        save_money -= 1

    else:
        num_toys += 1

total_money = save_money + (num_toys * prc_toy)

if total_money >= prc_wash_mash:
    print(f"Yes! {total_money - prc_wash_mash:.2f}")
else:
    print(f"No! {prc_wash_mash - total_money:.2f}")

