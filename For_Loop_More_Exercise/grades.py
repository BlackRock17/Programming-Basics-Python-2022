num_students = int(input())

low = 0
mid = 0
good = 0
very_good = 0
success = 0

for i in range(0, num_students):
    grade = float(input())

    if 2 <= grade < 3:
        low += 1
        success += grade
    elif 3 <= grade < 4:
        mid += 1
        success += grade
    elif 4 <= grade < 5:
        good += 1
        success += grade
    elif grade >= 5:
        very_good += 1
        success += grade

average_success = success / num_students

print(f"Top students: {very_good / num_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good / num_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {mid / num_students * 100:.2f}%")
print(f"Fail: {low / num_students * 100:.2f}%")
print(f"Average: {average_success:.2f}")





