actor = input()
start_points = float(input())
evaluative = int(input())

actor_points = start_points

for i in range(0, evaluative):
    name = input()
    points = float(input())

    actor_points += len(name) * points / 2

    if actor_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {actor_points:.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {1250.5 - actor_points:.1f} more!")


