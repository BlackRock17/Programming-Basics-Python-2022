num_location = int(input())

for i in range(0, num_location):
    total_yield = 0
    expected_yield = float(input())
    days = int(input())

    for j in range(0, days):
        mined_gold = float(input())

        total_yield += mined_gold

    average_yield = total_yield / days

    if average_yield >= expected_yield:
        print(f"Good job! Average gold per day: {average_yield:.2f}.")
    else:
        print(f"You need {expected_yield - average_yield:.2f} gold.")
