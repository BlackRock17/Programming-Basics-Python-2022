num1 = input()
num2 = input()

digit1_1 = int(num1[0])
digit1_2 = int(num1[1])
digit1_3 = int(num1[2])
digit1_4 = int(num1[3])
digit2_1 = int(num2[0])
digit2_2 = int(num2[1])
digit2_3 = int(num2[2])
digit2_4 = int(num2[3])

for i in range(digit1_1, digit2_1 + 1):
    if i % 2 == 0:
        continue
    for j in range(digit1_2, digit2_2 + 1):
        if j % 2 == 0:
            continue
        for k in range(digit1_3, digit2_3 + 1):
            if k % 2 == 0:
                continue
            for l in range(digit1_4, digit2_4 + 1):
                if l % 2 == 0:
                    continue
                else:
                    print(f"{i}{j}{k}{l}", end=" ")
