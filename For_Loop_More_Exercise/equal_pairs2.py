pairs = int(input())
first_pair = int(input()) + int(input())

current_sum = 0
max_diff = 0

for i in range(0, pairs - 1):
    current_sum = int(input()) + int(input())

    if abs(current_sum - first_pair) > max_diff:
        max_diff = abs(current_sum - first_pair)

    first_pair = current_sum

if max_diff == 0:
    print(f"Yes, value={first_pair}")
else:
    print(f"No, maxdiff={max_diff}")