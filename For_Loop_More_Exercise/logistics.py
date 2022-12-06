num_cargo = int(input())

ton = 0
van = 0
lorry = 0
train = 0

for i in range(0, num_cargo):
    cargo = int(input())

    if cargo <= 3:
        ton += cargo
        van += cargo

    elif 4 <= cargo <= 11:
        ton += cargo
        lorry += cargo

    else:
        ton += cargo
        train += cargo

averaged_price = (van * 200 + lorry * 175 + train * 120) / ton

print(f"{averaged_price:.2f}")
print(f"{van / ton * 100:.2f}%")
print(f"{lorry / ton * 100:.2f}%")
print(f"{train / ton * 100:.2f}%")

