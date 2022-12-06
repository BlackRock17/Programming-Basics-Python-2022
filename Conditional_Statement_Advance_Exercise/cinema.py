projection_type = input()
rows = int(input())
columns = int(input())
income = 0

premiere = 12
normal = 7.5
discount = 5

capacity = rows * columns

if projection_type == "Premiere":
    income = capacity * premiere
elif projection_type == "Normal":
    income = capacity * normal
elif projection_type == "Discount":
    income = capacity * discount

print(f"{income:.2f} leva")

