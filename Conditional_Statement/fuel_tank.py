fuel = input()
ltr_left = float(input())

if fuel == "Diesel":
    if ltr_left >= 25:
        print("You have enough diesel.")
    elif ltr_left < 25:
        print("Fill your tank with diesel!")
elif fuel == "Gasoline":
    if ltr_left >= 25:
        print("You have enough gasoline.")
    elif ltr_left < 25:
        print("Fill your tank with gasoline!")
elif fuel == "Gas":
    if ltr_left >= 25:
        print("You have enough gas.")
    elif ltr_left < 25:
        print("Fill your tank with gas!")
else:
    print("Invalid fuel!")

