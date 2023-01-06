total_meters = 5364
days = 0

while True:
    sleep = input()

    if sleep == "END":
        print("Failed!")
        print(f"{total_meters}")
        break

    if sleep == "Yes" and total_meters == 5364:
        days += 2

    if sleep == "Yes" and total_meters != 5364:
        days += 1

    if days > 5:
        print("Failed!")
        print(f"{total_meters}")
        break

    meters_traveled = int(input())
    total_meters += meters_traveled

    if total_meters >= 8848:
        print(f"Goal reached for {days} days!")
        break