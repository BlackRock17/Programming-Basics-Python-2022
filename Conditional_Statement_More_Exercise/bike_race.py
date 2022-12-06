num_juniors = int(input())
num_seniors = int(input())
route = input()

sum = 0

if route == "trail":
    sum = (num_juniors * 5.5) + (num_seniors * 7)
elif route == "cross-country":
    sum = (num_juniors * 8) + (num_seniors * 9.5)
    if num_juniors + num_seniors >= 50:
        sum *= 0.75
elif route == "downhill":
    sum = (num_juniors * 12.25) + (num_seniors * 13.75)
elif route == "road":
    sum = (num_juniors * 20) + (num_seniors * 21.5)

print(f"{sum * 0.95:.2f}")
