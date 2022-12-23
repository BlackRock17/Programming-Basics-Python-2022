import math
from math import floor

record_sec = float(input())
distance_m = float(input())
sec_for_1m = float(input())

racer_time = 0

racer_time = distance_m * sec_for_1m

racer_time += math.floor(distance_m / 50) * 30

if racer_time < record_sec:
    print(f"Yes! The new record is {racer_time:.2f} seconds.")
else:
    print(f"No! He was {racer_time - record_sec:.2f} seconds slower.")
