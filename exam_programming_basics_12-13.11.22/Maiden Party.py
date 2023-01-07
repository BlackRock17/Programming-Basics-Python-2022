party = float(input())
num_love = int(input())
num_rose = int(input())
num_keyholder = int(input())
num_cartoons = int(input())
num_lucky = int(input())

total_sum = (num_love * 0.6) + (num_rose * 7.2) + (num_keyholder * 3.6) + (num_cartoons * 18.2) + (num_lucky * 22)
counter = num_love + num_rose + num_keyholder + num_cartoons + num_lucky

if counter >= 25:
    total_sum *= 0.65

total_sum *= 0.9

if total_sum >= party:
    print(f"Yes! {total_sum - party:.2f} lv left.")
else:
    print(f"Not enough money! {party - total_sum:.2f} lv needed.")


