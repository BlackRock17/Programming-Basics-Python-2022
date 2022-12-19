days = int(input())
hours_per_day = int(input())

total = 0

for day in range(1, days + 1):
    day_sum = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0:
            if hour % 2 == 1:
                day_sum += 2.5
            else:
                day_sum += 1
        else:
            if hour % 2 == 0:
                day_sum += 1.25
            else:
                day_sum += 1
    total += day_sum
    print(f"Day: {day} - {day_sum:.2f} leva")

print(f"Total: {total:.2f} leva")






