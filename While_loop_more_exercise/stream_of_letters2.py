symbol = ""
message = ""
c_counter = 0
o_counter = 0
n_counter = 0

while True:
    if c_counter == 1 and o_counter == 1 and n_counter == 1:
        symbol += " "
        message = symbol
        c_counter = 0
        o_counter = 0
        n_counter = 0
        continue

    command = input()

    if command == "End":
        break

    if 97 <= ord(command) <= 122 or 65 <= ord(command) <= 90:

        if command == "c" and c_counter < 1:
            c_counter += 1
            continue

        elif command == "o" and o_counter < 1:
            o_counter += 1
            continue

        elif command == "n" and n_counter < 1:
            n_counter += 1
            continue

        symbol += command
print(message)



