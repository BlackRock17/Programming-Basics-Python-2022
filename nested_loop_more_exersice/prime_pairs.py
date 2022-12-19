from math import sqrt

first_pair = int(input())
second_pair = int(input())
first_diff = int(input())
second_diff = int(input())

for pair1 in range(first_pair, first_pair + first_diff + 1):
    for pair2 in range(second_pair, second_pair + second_diff + 1):
        is_prime = True

        sqrt_pair1 = int(sqrt(pair1))
        sqrt_pair2 = int(sqrt(pair2))

        for i in range(2, sqrt_pair1 + 1):
            if pair1 % i == 0:
                is_prime = False
                break

        for j in range(2, sqrt_pair2 + 1):
            if pair2 % j == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{pair1}{pair2}")
















