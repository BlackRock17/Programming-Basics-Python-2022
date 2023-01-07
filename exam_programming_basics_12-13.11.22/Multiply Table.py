num = int(input())

last_digit = num % 10
num = num // 10
second_digit = num % 10
num = num // 10
first_digit = num % 10

for i in range(1, last_digit + 1):
    for j in range(1, second_digit + 1):
        for k in range(1, first_digit + 1):

            print(f"{i} * {j} * {k} = {i * j * k};")


