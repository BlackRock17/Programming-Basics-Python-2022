win_match = 0
lost_match = 0
counter = 0

while True:
    name = input()


    if name == "End of tournaments":
        print(f"{win_match / counter * 100:.2f}% matches win")
        print(f"{lost_match / counter * 100:.2f}% matches lost")
        break

    tournament = int(input())

    for game in range(1, tournament + 1):
        counter += 1
        win_points = int(input())
        lost_points = int(input())

        if win_points > lost_points:
            win_match += 1
            print(f"Game {game} of tournament {name}: win with {win_points - lost_points} points.")
        else:
            lost_match += 1
            print(f"Game {game} of tournament {name}: lost with {lost_points - win_points} points.")





