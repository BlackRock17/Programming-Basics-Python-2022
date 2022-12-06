budget = float(input())
category = input()
num_of_people = int(input())

transport = 0
prc_VIP = 499.99
prc_normal = 249.99

if 1 <= num_of_people <= 4:
    transport = budget * 0.75
elif 5 <= num_of_people <= 9:
    transport = budget * 0.6
elif 10 <= num_of_people <= 24:
    transport = budget * 0.5
elif 25 <= num_of_people <= 49:
    transport = budget * 0.4
elif num_of_people >= 50:
    transport = budget * 0.25

total_left = budget - transport
price = 0

if category == "VIP":
    price = num_of_people * prc_VIP
elif category == "Normal":
    price = num_of_people * prc_normal

if total_left >= price:
    print(f"Yes! You have {total_left - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - total_left:.2f} leva.")
