count_steps = 0

while count_steps < 10000:
    action = input()

    if action == "Going home":
        last_steps = int(input())
        count_steps += last_steps
        break

    steps = int(action)
    count_steps += steps

if count_steps < 10000:
    print(f"{10000 - count_steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{count_steps - 10000} steps over the goal!")

