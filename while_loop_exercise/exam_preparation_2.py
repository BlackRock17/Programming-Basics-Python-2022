failed_threshold = int(input())

failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = None

while failed_times < failed_threshold:
    problem_name = input()

    if problem_name == "Enough":
        print(f"Average score: {grades_sum / solved_problems_count:.2f}")
        print(f"Number of problems: {solved_problems_count}")
        print(f"Last problem: {last_problem}")
        break

    problem_name = last_problem

    grade = int(input())

