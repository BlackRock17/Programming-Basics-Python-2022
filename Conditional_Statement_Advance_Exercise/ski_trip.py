days = int(input())
room = input()
rating = input()

nights = days - 1

prc_room = 18
prc_apartment = 25
prc_pr_apartment = 35

total = 0

if room == "room for one person":
    total = nights * prc_room
elif room == "apartment":
    if days < 10:
        total = (nights * prc_apartment) * 0.7
    elif 10 <= days <= 15:
        total = (nights * prc_apartment) * 0.65
    elif days > 15:
        total = (nights * prc_apartment) * 0.5
elif room == "president apartment":
    if days < 10:
        total = (nights * prc_pr_apartment) * 0.9
    elif 10 <= days <= 15:
        total = (nights * prc_pr_apartment) * 0.85
    elif days > 15:
        total = (nights * prc_pr_apartment) * 0.8

if rating == "positive":
    total *= 1.25
elif rating == "negative":
    total *= 0.9

print(f"{total:.2f}")

