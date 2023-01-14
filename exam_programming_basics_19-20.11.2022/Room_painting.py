import math

paint = int(input())
wallpaper = int(input())
prc_gloves = float(input())
prc_brush = float(input())

gloves = math.ceil(wallpaper * 0.35)
brush = math.floor(paint * 0.48)

total = (paint * 21.5) + (wallpaper * 5.2) + (gloves * prc_gloves) + (brush * prc_brush)

print(f"This delivery will cost {total / 15:.2f} lv.")


