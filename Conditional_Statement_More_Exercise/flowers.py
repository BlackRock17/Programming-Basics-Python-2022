num_chrysanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()
day = input()

prc_bouquet = 0

if season == "Spring" or season == "Summer":
    prc_bouquet = (num_chrysanthemums * 2) + (num_roses * 4.1) + (num_tulips * 2.5)
    if season == "Spring" and num_tulips > 7:
        prc_bouquet *= 0.95

elif season == "Autumn" or season == "Winter":
    prc_bouquet = (num_chrysanthemums * 3.75) + (num_roses * 4.5) + (num_tulips * 4.15)
    if season == "Winter" and num_roses >= 10:
        prc_bouquet *= 0.9

if day == "Y":
    prc_bouquet *= 1.15

if num_roses + num_tulips + num_chrysanthemums > 20:
    prc_bouquet *= 0.8

print(f"{prc_bouquet + 2:.2f}")

