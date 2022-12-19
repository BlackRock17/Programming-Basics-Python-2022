num1 = int(input())
num2 = int(input())
num3 = int(input())

for i in range(2, num1 + 1, 2):
    for j in range(1, num2 + 1):
        if j == 1 or j == 4 or j == 6 or j > 7:
            continue
        for k in range(2, num3 + 1, 2):

            print(f"{i} {j} {k}")