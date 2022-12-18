total_kids = 0
total_student = 0
total_standard = 0

while True:
    name = input()

    if name == "Finish":
        break

    capacity = int(input())
    sold_ticket = 0

    while sold_ticket < capacity:
        type_ticket = input()

        if type_ticket == "End":
            break
        elif type_ticket == "student":
            total_student += 1
        elif type_ticket == "standard":
            total_standard += 1
        elif type_ticket == "kid":
            total_kids += 1

        sold_ticket += 1

    print(f"{name} - {sold_ticket / capacity * 100:.2f}% full.")

total_tickets = total_kids + total_student + total_standard

print(f"Total tickets: {total_tickets}")
print(f"{total_student / total_tickets * 100:.2f}% student tickets.")
print(f"{total_standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{total_kids / total_tickets * 100:.2f}% kids tickets.")
