prime_sum = 0
non_prime_sum = 0

while True:
    user_input = input()

    if user_input == "stop":
        print(f"Sum of all prime numbers is: {prime_sum}")
        print(f"Sum of all non prime numbers is: {non_prime_sum}")
        break

    number = int(user_input)

    if number < 0:
        print("Number is negative.")
        continue

    is_number = False

    for i in range(2, number):
        if number % i == 0:
            is_number = True

    if is_number:
        non_prime_sum += number
    else:
        prime_sum += number





