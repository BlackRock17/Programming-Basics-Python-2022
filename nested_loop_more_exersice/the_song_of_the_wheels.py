number = int(input())

counter = 0
is_password = False
password = 0

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):

                if (num1 * num2) + (num3 * num4) != number:
                    continue
                elif num1 >= num2:
                    continue
                elif num3 <= num4:
                    continue
                else:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")
                    counter += 1
                    if counter == 4:
                        is_password = True
                        password = (num1 * 1000) + (num2 * 100) + (num3 * 10) + num4
print("")

if is_password:
    print(f"Password: {password}")
else:
    print("No!")




