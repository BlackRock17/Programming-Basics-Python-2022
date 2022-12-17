starting_num = int(input())
end = int(input())
magic_num = int(input())

counter = 0
is_magic = False

for i in range (starting_num, end + 1):
    for j in range (starting_num, end + 1):
        counter += 1
        if i + j == magic_num:
            is_magic = True
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            break
    if is_magic:
        break

else:
    print(f"{counter} combinations - neither equals {magic_num}")


