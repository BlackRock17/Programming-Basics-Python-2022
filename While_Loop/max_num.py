max_num = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    current_num = int(user_input)
    if current_num > max_num:
        max_num = current_num

print(max_num)
