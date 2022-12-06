time = int(input())
day = input()

if time >= 10 and time <=18 and day != "Sunday":
    print("open")
else:
    print("closed")
