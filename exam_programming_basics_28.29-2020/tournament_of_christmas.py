days = int(input())

total_money = 0
day_win = 0
day_lose = 0

for day in range(0, days):
    win = 0
    lose = 0
    day_money = 0
    while True:
        game = input()
        if game == "Finish":
            if win > lose:
                day_money *= 1.1
            total_money += day_money
            day_win += win
            day_lose += lose
            break

        result = input()
        if result == "win":
            win += 1
            day_money += 20
        else:
            lose += 1

if day_win > day_lose:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")


