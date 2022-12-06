deposit = float(input())
deposit_deadline = int(input())
yearly_percent = float(input()) / 100

total = deposit + deposit_deadline * ((deposit * yearly_percent) / 12)

print(total)
