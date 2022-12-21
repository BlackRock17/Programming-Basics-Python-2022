name = input()

total_points = 301
successful_shots = 0
unsuccessful_shots = 0

while True:
    field = input()

    if field == "Retire":
        print(f"{name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())

    if field == "Triple":
        points *= 3
    elif field == "Double":
        points *= 2

    if points <= total_points:
        total_points -= points
        successful_shots += 1
    else:
        unsuccessful_shots += 1

    if total_points == 0:
        print(f"{name} won the leg with {successful_shots} shots.")
        break





