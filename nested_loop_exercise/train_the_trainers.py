people = int(input())

final_assessment = 0
counter = 0

while True:
    presentation = input()

    if presentation == "Finish":
        print(f"Student's final assessment is {final_assessment / counter:.2f}.")
        break

    total_grades = 0

    for i in range(people):
        grades = float(input())

        total_grades += grades
        final_assessment += grades
        counter += 1

    print(f"{presentation} - {total_grades / people:.2f}.")




