x = float(input())
y = float(input())
h = float(input())

side_wall = x * y * 2
side_wall -= 4.5

back_wall = x * x * 2
back_wall -= 2.4

area_first = side_wall + back_wall

green_paint = area_first / 3.4

roof_side = x * y * 2
roof_front = (x * h / 2) * 2

area_roof = roof_side + roof_front

red_paint = area_roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")

