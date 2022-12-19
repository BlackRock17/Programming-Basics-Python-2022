first_max = int(input())
second_max = int(input())
max_num_pass = int(input())

simbol_A = 35
simbol_B = 64

for i in range(1, first_max + 1):
    for j in range(1, second_max + 1):
        if max_num_pass == 0:
            exit()
        print(f"{chr(simbol_A)}{chr(simbol_B)}{i}{j}{chr(simbol_B)}{chr(simbol_A)}", end="|")
        max_num_pass -= 1
        simbol_A += 1
        simbol_B += 1
        if simbol_A == 56:
            simbol_A = 35
        if simbol_B == 97:
            simbol_B = 64



