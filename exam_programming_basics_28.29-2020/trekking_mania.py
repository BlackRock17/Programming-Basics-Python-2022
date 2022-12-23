num_groups = int(input())

musalla = 0
montblanc = 0
kilimajaro = 0
k2 = 0
everest = 0
total_people = 0

for i in range (0, num_groups):
    num_people = int(input())

    if num_people < 6:
        musalla += num_people
    elif 6 <= num_people < 13:
        montblanc += num_people
    elif 13 <= num_people < 26:
        kilimajaro += num_people
    elif 26 <= num_people < 41:
        k2 += num_people
    elif num_people >= 41:
        everest += num_people

    total_people += num_people

print(f"{musalla / total_people * 100:.2f}%")
print(f"{montblanc / total_people * 100:.2f}%")
print(f"{kilimajaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")
