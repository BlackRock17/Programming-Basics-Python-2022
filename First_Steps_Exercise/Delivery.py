chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chicken_price = 10.35
fish_price = 12.40
veg_price = 8.15
delivery = 2.50

menu_price = (chicken_menu * chicken_price) + (fish_menu * fish_price) + (veg_menu * veg_price)

dessert_price = menu_price * 0.20

total = menu_price + dessert_price + delivery

print(total)