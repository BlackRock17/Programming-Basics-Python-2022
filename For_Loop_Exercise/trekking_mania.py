num_groups = int(input())

musalla = 0
montblanc = 0
kilimanjaro = 0
k2 =0
everest = 0

total_people = 0

for i in range(0, num_groups):
    num_people = int(input())

    if 0 < num_people <= 5:
        musalla += num_people
        total_people += num_people

    elif 5 < num_people <= 12:
        montblanc += num_people
        total_people += num_people

    elif 12 < num_people <= 25:
        kilimanjaro += num_people
        total_people += num_people

    elif 25 < num_people <= 40:
        k2 += num_people
        total_people += num_people

    else:
        everest += num_people
        total_people += num_people

print(f"{musalla / total_people * 100:.2f}%")
print(f"{montblanc / total_people * 100:.2f}%")
print(f"{kilimanjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")
