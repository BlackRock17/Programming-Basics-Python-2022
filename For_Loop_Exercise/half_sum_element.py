import sys

num_of_numbers = int(input())

max_num = -sys.maxsize
sum = 0

for i in range(0, num_of_numbers):
    number = int(input())

    if number > max_num:
        max_num = number

    sum += number

if max_num == sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - (sum - max_num))}")

