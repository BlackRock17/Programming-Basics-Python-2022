from math import pow

n = int(input())

for one in range(0, n):
    if one % 2 == 0:
        print(int(pow(2, one)))



