name = input()

evaluation = 0
current_grade = 0
fails = 0

while True:
    current_evaluation = float(input())

    if current_evaluation < 4:
        fails += 1
        if fails == 2:
            break
        continue

    if current_evaluation >= 4:
        current_grade += 1
        evaluation += current_evaluation

    if current_grade >= 12:
        break

average_evaluation = evaluation / 12

if fails >= 2:
    print(f"{name} has been excluded at {current_grade + 1} grade")
else:
    print(f"{name} graduated. Average grade: {average_evaluation:.2f}")


