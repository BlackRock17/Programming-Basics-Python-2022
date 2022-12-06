capacity = int(input())
fans = int(input())

A = 0
B = 0
V = 0
G = 0

for i in range(0, fans):
    sector = input()

    if sector == "A":
        A += 1
    elif sector == "B":
        B += 1
    elif sector == "V":
        V += 1
    elif sector == "G":
        G += 1

print(f"{A / fans * 100:.2f}%")
print(f"{B / fans * 100:.2f}%")
print(f"{V / fans * 100:.2f}%")
print(f"{G / fans * 100:.2f}%")
print(f"{fans / capacity * 100:.2f}%")


