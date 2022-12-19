from math import sqrt

num = int(input())

sqrt_num = int(sqrt(num))

is_prime = True

for i in range(2, sqrt_num + 1):
    if num / i == num // i:
        is_prime = False


print(is_prime)