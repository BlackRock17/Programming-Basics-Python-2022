width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

while True:
    cartons = input()

    if cartons == "Done":
        print(f"{free_space} Cubic meters left.")
        break

    filled_space = int(cartons)
    free_space -= filled_space

    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break

