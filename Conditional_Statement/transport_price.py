num_km = int(input())
d_or_n = input()

prc_train = 0.06 * num_km
prc_bus = 0.09 * num_km
prc_taxi_day = 0.70 + (0.79 * num_km)
prc_taxi_night = 0.70 + (0.90 * num_km)

if num_km >= 100:
    print(f"{prc_train:.2f}")
elif num_km >= 20:
    print(f"{prc_bus:.2f}")
elif num_km < 20 and d_or_n == "day":
    print(f"{prc_taxi_day:.2f}")
elif num_km < 20 and d_or_n == "night":
    print(f"{prc_taxi_night:.2f}")
