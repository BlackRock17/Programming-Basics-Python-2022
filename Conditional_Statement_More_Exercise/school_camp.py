season = input()
type_group = input()
num_student = int(input())
num_nights = int(input())

prc_nights = 0
sport = ""

if season == "Winter":
    if type_group == "boys" or type_group == "girls":
        prc_nights = num_student * 9.6 * num_nights
    elif type_group == "mixed":
        prc_nights = num_student * 10 * num_nights
    if type_group == "boys":
        sport = "Judo"
    elif type_group == "girls":
        sport = "Gymnastics"
    elif type_group == "mixed":
        sport = "Ski"

elif season == "Spring":
    if type_group == "boys" or type_group == "girls":
        prc_nights = num_student * 7.2 * num_nights
    elif type_group == "mixed":
        prc_nights = num_student * 9.5 * num_nights
    if type_group == "boys":
        sport = "Tennis"
    elif type_group == "girls":
        sport = "Athletics"
    elif type_group == "mixed":
        sport = "Cycling"

elif season == "Summer":
    if type_group == "boys" or type_group == "girls":
        prc_nights = num_student * 15 * num_nights
    elif type_group == "mixed":
        prc_nights = num_student * 20 * num_nights
    if type_group == "boys":
        sport = "Football"
    elif type_group == "girls":
        sport = "Volleyball"
    elif type_group == "mixed":
        sport = "Swimming"

if 10 <= num_student < 20:
    prc_nights *= 0.95
elif 20 <= num_student < 50:
    prc_nights *= 0.85
elif num_student >= 50:
    prc_nights *= 0.5

print(f"{sport} {prc_nights:.2f} lv.")



