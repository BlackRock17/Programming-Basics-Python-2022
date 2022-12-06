w = float(input())
h = float(input())


w *= 100
h *= 100
h -= 100

place_lenght = w // 120
place_width = h // 70

all_place = place_lenght * place_width

all_place -= 3

print(int(all_place))


