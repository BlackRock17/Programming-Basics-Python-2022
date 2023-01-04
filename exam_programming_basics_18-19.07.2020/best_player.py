best_player = ""
goal = 0

while True:
    name = input()

    if name == "END":
        break

    num_goals = int(input())

    if num_goals > 9:
        goal = num_goals
        best_player = name
        break
    elif num_goals > goal:
        goal = num_goals
        best_player = name

print(f"{best_player} is the best player!")

if goal > 2:
    print(f"He has scored {goal} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goal} goals.")
