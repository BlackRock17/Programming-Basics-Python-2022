days = 365
holidays = int(input())

play_day_off = holidays * 127
play_day_on = (days - holidays) * 63
total_play_min = play_day_off + play_day_on

if total_play_min > 30000:
    hours = (total_play_min - 30000) // 60
    min = (total_play_min - 30000) % 60
    print(f"Tom will run away")
    print(f"{hours} hours and {min} minutes more for play")
elif total_play_min <= 30000:
    hours = (30000 - total_play_min) // 60
    min = (30000 - total_play_min) % 60
    print(f"Tom sleeps well")
    print(f"{hours} hours and {min} minutes less for play")


