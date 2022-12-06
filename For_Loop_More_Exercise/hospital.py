days = int(input())

doctors = 7

examined = 0
unexamined = 0

for day in range(1, days + 1):
    patients = int(input())

    if day % 3 == 0 and unexamined > examined:
        doctors += 1

    if patients <= doctors:
        examined += patients
    elif patients > doctors:
        examined += doctors
        unexamined += patients - doctors

print(f"Treated patients: {examined}.")
print(f"Untreated patients: {unexamined}.")







