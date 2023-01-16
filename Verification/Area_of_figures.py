from math import pi

figure = input()
area = 0

if figure == "square":
    side = float(input())
    area = side * side

elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif figure == "circle":
    radius = float(input())
    area = radius * radius * pi

elif figure == "triangle":
    side = float(input())
    length = float(input())
    area = side * length / 2

print(f"{area:.3f}")

