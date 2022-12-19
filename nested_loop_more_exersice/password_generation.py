num = int(input())
num2 = int(input())

for i in range(1, num + 1):
    for j in range(1, num + 1):
        for k in range(97, 97 + num2):
            for l in range(97, 97 + num2):
                for m in range(1, num + 1):

                    if m > j and m > i:
                        print(f"{i}{j}{chr(k)}{chr(l)}{m}", end=" ")