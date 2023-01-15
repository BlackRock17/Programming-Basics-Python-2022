import math

width = float(input())
length = float(input())
height = float(input())
height_astronaut = float(input())

cub_volume = width * length * height

room_space = (height_astronaut + 0.4) * 2 * 2

total_space = math.floor(cub_volume / room_space)

if total_space >= 3 and total_space <= 10:
    print(f"The spacecraft holds {total_space} astronauts.")
elif total_space < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
