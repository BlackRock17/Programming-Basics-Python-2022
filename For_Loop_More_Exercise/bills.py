months = int(input())

electricity = 0

for i in range(0, months):
    electricity_prc = float(input())

    electricity += electricity_prc

other = (months * 20 + months * 15 + electricity) * 1.2

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {months * 20:.2f} lv")
print(f"Internet: {months * 15:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {(other + electricity + months * 35) / months:.2f} lv")



