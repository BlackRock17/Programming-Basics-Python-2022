a1 = int(input())
a2 = int(input())
n = int(input())
n3 = int(n / 2)

for i in range(a1, a2):
    if i % 2 == 0:
        continue
    for j in range(1, n):
        for k in range(1, n3):
            if (j + k + i) % 2 == 0:
                continue
            else:
                print(f"{chr(i)}-{j}{k}{i}")

