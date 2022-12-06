from math import floor

tournaments = int(input())
starting_points = int(input())


player_points = starting_points
num_tour = 0
win = 0
for i in range(0, tournaments):
    final = input()

    if final == "W":
        player_points += 2000
        num_tour += 1
        win += 1
    elif final == "F":
        player_points += 1200
        num_tour += 1
    elif final == "SF":
        player_points += 720
        num_tour += 1

average_points = (player_points - starting_points) / num_tour
percent_win = win / tournaments * 100

print(f"Final points: {player_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_win:.2f}%")

