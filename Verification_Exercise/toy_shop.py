price_excursion = float(input())
num_puzzels = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

prc_puzzel = 2.60
prc_doll = 3
prc_bear = 4.10
prc_minion = 8.20
prc_truck = 2

total_num_toys = num_puzzels + num_dolls + num_bears + num_minions + num_trucks

total_prc_toys = (num_puzzels * prc_puzzel) + (num_dolls * prc_doll) + \
                 (num_bears * prc_bear) + (num_minions * prc_minion) + \
                 (num_trucks * prc_truck)

if total_num_toys >= 50:
    total_prc_toys *= 0.75

rent = total_prc_toys * 0.10

total_profit = total_prc_toys - rent

if total_profit >= price_excursion:
    print(f"Yes! {total_profit - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - total_profit:.2f} lv needed.")

