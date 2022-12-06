min_num = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    current_num = int(user_input)
    if current_num < min_num:
        min_num = current_num

print(min_num)
