max_bad_grades = int(input())

bad_grades = 0
average_score = 0
num_of_problems = 0
last_problem = None

while True:
    problem = input()

    if problem == "Enough":
        print(f"Average score: {average_score / num_of_problems:.2f}")
        print(f"Number of problems: {num_of_problems}")
        print(f"Last problem: {last_problem}")
        break

    last_problem = problem
    grade = int(input())

    if grade <= 4:
        bad_grades += 1
        num_of_problems += 1
        average_score += grade
        if bad_grades == max_bad_grades:
            print(f"You need a break, {bad_grades} poor grades.")
            break
        continue

    if grade > 4:
        num_of_problems += 1
        average_score += grade

