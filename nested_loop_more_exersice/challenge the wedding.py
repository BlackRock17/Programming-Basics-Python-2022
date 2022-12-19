man = int(input())
woman = int(input())
table = int(input())

for i in range(1, man + 1):
    for j in range(1, woman + 1):
        if table == 0:
            exit()
        table -= 1
        print(f"({i} <-> {j})", end=" ")
