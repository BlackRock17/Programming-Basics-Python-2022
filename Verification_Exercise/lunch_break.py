import math

name = input()
duration_of_ep = int(input())
duration_of_bk = int(input())

lunch_time = duration_of_bk * 0.125
rest_time = duration_of_bk * 0.25
time_left = duration_of_bk - lunch_time - rest_time

if time_left >= duration_of_ep:
    print(f"You have enough time to watch {name} and left with"
          f" {math.ceil(time_left - duration_of_ep)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(duration_of_ep - time_left)} more minutes.")

