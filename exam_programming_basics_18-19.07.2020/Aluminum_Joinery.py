num_joinery = int(input())
type_joinery = input()
delivery = input()

total_prc = 0

if type_joinery == "90X130":
    total_prc = num_joinery * 110
    if 30 < num_joinery <= 60:
        total_prc *= 0.95
    elif num_joinery > 60:
        total_prc *= 0.92
elif type_joinery == "100X150":
    total_prc = num_joinery * 140
    if 40 < num_joinery <= 80:
        total_prc *= 0.94
    elif num_joinery > 80:
        total_prc *= 0.90
elif type_joinery == "130X180":
    total_prc = num_joinery * 190
    if 20 < num_joinery <= 50:
        total_prc *= 0.93
    elif num_joinery > 50:
        total_prc *= 0.88
elif type_joinery == "200X300":
    total_prc = num_joinery * 250
    if 25 < num_joinery <= 50:
        total_prc *= 0.91
    elif num_joinery > 50:
        total_prc *= 0.86

if delivery == "With delivery":
    total_prc += 60

if num_joinery > 99:
    total_prc *= 0.96

if num_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_prc:.2f} BGN")

