num_pages = int(input())
pages_for_1hour = int(input())
days = int(input())

total_time = num_pages / pages_for_1hour
total_days = total_time / days

print(int(total_days))

